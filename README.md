# AddToFile

[Sublime Text](https://www.sublimetext.com "Sublime Text") 3 plugin which allows for a selection to be instantly added to an open file


### Usage

When run, a panel appears containing a list of currently open files (excluding the current file). The content inside the selection will be copied to the end of the file selected from the panel. Note that the command will not be invoked if the selection is empty.

### Demonstration

![demo-1](assets/demonstration-1.png)
Demonstration with standard settings

![demo-2](assets/demonstration-2.png)
Demonstration with file previews set to true and file paths set to true


### Configuration

Edit the AddToFile.sublime-settings to configure this plugin

Setting                    | Description
--------------------------:|:------------
`suggest_new_file`         |Add an option to **create a new file** inside the file selection panel. Defaults to true.
`add_to_single_view`       |**Automatically select the view** in the file selection panel if there is only one view in the list. Defaults to false. <sup id="text1">[[1]](#footnote1)</sup>
`show_status_message`      |Show a **message in the status bar** when text is copied. Defaults to true
`show_file_path`           |Show the **full file path** instead of the file name in the file selection panel to help distinguish files with the same name in different directories. Defaults to false. <sup id="text2">[[2]](#footnote2)</sup>
`status_message`           |Set the **message to appear in the status bar**. Defaults to `Copied to {name}`. <sup id="text3">[[3]](#footnote3)</sup>
`keep_focus`               |Keep the **focus on the source file** when copying rather than switching to the destination file's view. Defaults to true.
`show_preview`             |Show a **3-line file preview** in the file selection panel. Defaults to false.
`scroll_view`              |**Scroll the view** to where the text was copied. Defaults to true. <sup id="text4">[[4]](#footnote4)</sup>

<a name="footnote1">1</a>: This will not work if `add_to_suggest_new_file` is set to true as this adds another element to the file list. Even if there is no other view open and 'New File' is the only item in the list, the panel will still open to ensure that a new file isn't accidentally created. [↑](#text1)

<a name="footnote2">2</a>: If there are two files called 'AddToFile.py' in different directories, the file selection panel will display 'AddToFile.py' twice if this setting is set to false. However, the order that appears in the selection panel is the order of the view tabs from left to right which means the files could be distinguished by looking at which one's view tab is furthest left/right. [↑](#text2)

<a name="footnote3">3</a>: Can include `{name}`, `{path}`, `{dir}`, `{sourcename}`, `{sourcepath}` and `{sourcedir}` which will be replaced with their corresponding values:

Segment     |Description
-----------:|--------------
 `name `     |file name
 `path`      |the path to the file including the file
 `dir`       |the path to the file excluding the file
 `sourcename`|source file name
 `sourcepath`|the path to the source file including the file
 `sourcedir `|the path to the source file excluding the file

 [↑](#text3)

<a name="footnote4">4</a>: `keep_focus` must be set to false to allow the view to switch.  [↑](#text4)


### Installation

AddToFile can be installed manually:
1. Download the [`.zip file`](https://github.com/nchauhan890/AddToFile/archive/master.zip "AddToFile.zip")
2. Unzip the `.zip` file
3. Rename to `AddToFile`
4. Move to the `Packages` directory which can be opened through `Preferences --> Browse Packages...`


### TODO:

- [x] test what `add_to_single_view` will do if there is no other view and `add_to_suggest_new_file` is set to true.
- [x] test what happens if `show_file_path` is set to true and there are 2 views with the same name in different directories.
- [x] add {dir} in `status message` and replace {path}.
- [x] implement `keep focus` as false and not just true.
- [x] amend default values in AddToFile.sublime-settings.
