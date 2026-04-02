import subprocess
from datetime import datetime
from pathlib import Path

import sublime
import sublime_plugin


def plugin_loaded():
    """
    Hook that is called by Sublime when plugin is loaded.
    """
    pass


def plugin_unloaded():
    """
    Hook that is called by Sublime when plugin is unloaded.
    """
    for key in list(globals().keys()):
        if "imagepaste" in key.lower():
            del globals()[key]


class ImagePasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("image-paste.sublime-settings")
        variables = self.view.window().extract_variables()

        if "file_path" not in variables:
            sublime.status_message("Could not paste image: please save file first")
            return

        now = datetime.now()
        almost_now = datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=now.hour,
            minute=now.minute,
            second=now.second,
        )
        name = almost_now.isoformat().replace(":", "-").replace("T", "-")

        try:
            destination_folder = Path(
                sublime.expand_variables(settings.get("folder"), variables)
            )
            destination_folder.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            sublime.status_message("Could not create destination folder: {}".format(e))
            return

        destination = destination_folder / "{}{}.{}".format(
            settings.get("name_prefix"), name, settings.get("name_suffix")
        )

        command = ["pngpaste", str(destination)]

        file = Path(variables.get("file_path"))
        relative_path = destination.relative_to(file)
        text_to_insert = "{}{}{}".format(
            settings.get("paste_prefix"),
            str(relative_path),
            settings.get("paste_suffix"),
        )

        try:
            subprocess.check_output(command)
            for region in self.view.sel():
                self.view.insert(edit, region.begin(), text_to_insert)
        except FileNotFoundError:
            sublime.error_message(
                "Could not paste image: 'pngpaste' not found. "
                "Please install it (e.g., brew install pngpaste)"
            )
        except subprocess.CalledProcessError:
            print("Paste failed. Was there no image in the clipboard?")
