# AddToFile

[Sublime Text](https://www.sublimetext.com "Sublime Text") 3 plugin which allows for a selection to be instantly added to an open file

### Usage

When run, a panel appears containing a list of currently open files (excluding the current file). The content inside the selection will be copied to the end of the file selected from the panel. Note that the command will not be invoked if the selection is empty.

### Configuration

Edit the AddToFile.sublime-settings to configure this plugin

`add_to_suggest_new_file`: Add an option to create a new file inside the file selection panel. Default set to true.
`add_to_single_view`: Automatically select the view in the file selection panel if there is only one view in the list. Note that this will not work if `add_to_suggest_new_file` is set to true as this adds another element to the file list. Default set to false
`show_status_message`: Show a message in the status bar when text is copied. Default set to true
`show_file_path`: Show the full file path instead of the file name in the file selection panel to help distinguish files with the same name in different directories. Default set to false.
`status_message`: Set the message to appear in the status bar. Can include {name}, {path}, {sourcename} and {sourcepath} which will be replaced with their corresponding values. Defaults to "Copied to {name}".
`keep_focus`: Keep the focus on the source file when copying rather than switching to the destination file's view. Defaults to true.
`show_preview`: Show a 3-line file preview in the file selection panel. Defaults to false.
`scroll_view`: Scroll the view to where the text was copied. Note that `keep_focus` must be set to false to allow the view to switch. Defaults to true.

### TODO:

- test what `add_to_single_view` will do if there is no other view and `add_to_suggest_new_file` is set to true.
- test what happens if `show_file_path` is set to true and there are 2 views with the same name in different directories.
- test handling of multiple views of the same file.
- add {dir} in `status message` and replace {path}.
- implement `keep focus` as false and not just true.
- amend default values in AddToFile.sublime-settings.
