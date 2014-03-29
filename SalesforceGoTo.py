import sublime, sublime_plugin, re

class SalesforceGoToCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view = self.view
        viewSize = self.view.size()
        print("View size is " + str(viewSize))
        fullRegion = sublime.Region(0, viewSize)
        lineRegions = self.view.lines(fullRegion)
        print("View contains " + str(len(lineRegions)) + " lines")
        # regex = "\sit\(['\"]+(.*)['\"], function\("
        # patt = re.compile(regex)

        # self.specNameArr = []
        # self.specRegionArr = []

        # for region in lineRegions :
        #     lineContents = self.view.substr(region)
        #     matcher = patt.match(lineContents)
        #     if matcher is not None :
        #         specName = matcher.group(1)
        #         self.specNameArr.append(specName)
        #         self.specRegionArr.append(region)
        #         print("Found spec name: " + specName)

        # self.view.window().show_quick_panel(self.specNameArr, self.showSpec