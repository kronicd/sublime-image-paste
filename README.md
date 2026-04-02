# Image Paste

Sublime Text plugin for pasting images from the clipboard. Utilizes the
[pngpaste](https://github.com/jcsalterego/pngpaste) utility for the pasting
functionality, because the clipboard within Sublime only supports strings:
no binary data. So that's why this plugin is currently macOS only.

## Installation

### Manual Installation
1.  Open Sublime Text and go to `Preferences > Browse Packages...`.
2.  In the terminal, navigate to that directory and clone this repository:
    ```sh
    git clone https://github.com/kronicd/sublime-image-paste.git image-paste
    ```
3.  Install the `pngpaste` utility via Homebrew:
    ```sh
    brew install pngpaste
    ```

## Usage

Use the command: 'image-paste: Paste image' (Default key-binding set to
`CMD+OPTION+V`) to paste the image. Use the settings to adjust the destination
and the string that will be inserted into the text.

The plugin will automatically create the destination folder if it doesn't already exist.

## Settings

To customize the plugin, go to `Preferences > Package Settings > Image Paste > Settings`. It is recommended to copy these to your `User` settings:

*   `folder`: The directory where the image will be stored. Supports variables like `${file_path}` and `${file_base_name}`.
*   `paste_prefix` and `paste_suffix`: Prefix and suffix for the text that will be inserted into the current view.
*   `name_suffix`: Output format. Valid values are `png`, `gif`, `jpeg`, and `tiff`.

### Example: Markdown Image Tags
To insert a full Markdown image tag in a subfolder with the same name as your file:
```json
{
    "folder": "${file_path}/${file_base_name}",
    "paste_prefix": "![image](",
    "paste_suffix": ")"
}
```

## Requirements

*   **macOS**: This plugin currently only supports macOS.
*   **Sublime Text 4**: This version uses Python 3.8 (forced via `.python-version`).
*   **pngpaste**: Must be installed on your system.
