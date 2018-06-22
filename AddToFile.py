import sublime
import sublime_plugin


class AddToCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # text = sublime.Region(0, view.size())
        window = self.view.window()
        view = self.view
        sel = view.sel()
        # s = ''
        # for region in view.sel():
        #     if not region.empty():
        #         s += '\n' + view.substr(region)
        # print(s)
        for v in window.views():
            print(v.name())
            if v.name() == 'untitled':
                f = v
                break
        else:  # if no break occurs --> no current view called [untitled]
            f = window.new_file()
        f.set_name('untitled')
        # print(self)
        # print(edit)
        # print(f)
        window.focus_view(f)

        f.run_command('ins', {"selection":
                              [view.substr(s) for s in sel]})


class InsCommand(sublime_plugin.TextCommand):
    def run(self, edit, selection):
        edit = self.view.begin_edit('ins')
        # self.count = 0  # not using enumerate as it goes through 2 loops
        for line in selection:
            for char in line:
                self.insert(edit, self.view.size(), char)
                # self.count += 1
            self.insert(edit, self.view.size(), '\n')
            # self.count += 1
        self.view.end_edit(edit)
