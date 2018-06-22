import os

import sublime
import sublime_plugin


class AddToCommand(sublime_plugin.TextCommand):
    def __init__(self):
        self.settings = sublime.load_settings('AddT.sublime-settings')
        # load settings

    def on_done(self, val):
        if val == -1:
            return  # end if called with -1 value
        if self.items[val] == 'New File':
            # if the selected option is 'New File',
            # create a new file
            f = sublime.active_window().new_file()

        else:  # selected item isn't a file so must be 'new file'
            f = self.items[val]
        # sublime.active_window().focus_view(f)
        f.run_command('insert_to_end',
                      {"selection": [self.view.substr(s)
                                     for s in self.view.sel()]})
        # run insert command to add text

        string = self.settings.get('status_message',
                                   'Copied to {name}').format(
                                   os.path.split(f.file_name())[1])
        # set string with the name of the file that was copied to
        if self.settings.get('show_status_message', False):
            # run status bar message command if value specified
            # in settings
            sublime.active_window().run_command('add_status_bar_msg',
                                                {"msg": string})

    def run(self, edit):
        if not ''.join(self.view.substr(s) for s in self.view.sel()):
            return  # end if the selection is empty

        self.items = [view
                      for view in sublime.active_window().views()
                      if view.file_name()
                      if view != sublime.active_window().active_view()]
        # add list of views, excluding the current view

        if self.settings.get('add_to_suggest_new_file', False):
            self.items.append('New File')
            # add 'new file' option if specified settings

        # print(self.items)
        # print(os.path.split(self.view.file_name())[1])
        if self.settings.get('add_to_single_view', False) and len(self.items) == 1:
            self.on_done(0)
            # auto-run on_done if there's only 1 other view and if specified
            # in settings
        else:
            sublime.active_window().show_quick_panel([os.path.split(view.file_name())[1]
                                                     for view in self.items],
                                                     self.on_done)
            # show popup with the file names
            # (and 'New File' if specified in settings)


class InsertToEndCommand(sublime_plugin.TextCommand):
    def run(self, edit, lines):
        for line in lines:
            # insert lines to end of file
            self.view.insert(edit, self.view.size(), line)
            self.view.insert(edit, self.view.size(), '\n')


class AddStatusBarMsg(sublime_plugin.WindowCommand):
    def run(self, msg):
        # set the status bar message
        sublime.status_message(msg)
