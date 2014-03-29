import sublime, sublime_plugin, re, os, os.path

class SalesforceGoToCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.sel()) == 1:
            word = self.view.substr(self.view.word(self.view.sel()[0]))
            self.matchingFilePaths = self.getFilePaths(word) 
            if len(self.matchingFilePaths) == 1:
                self.view.window().open_file(self.matchingFilePaths[0])
            elif len(self.matchingFilePaths) > 1:
                self.view.window().show_quick_panel(self.matchingFilePaths, lambda index: self.view.window().open_file(self.matchingFilePaths[index]))
            else:
                sublime.message_dialog("Cannot find file that matches name '" + word + "'")
        else:
            print("Error: No word highlighted")

    # Get full path(s) of given file name. E.g. if given "Home" search for
    # "Home.cls" or "Home.page" in subdirectories of the "src" directory
    def getFilePaths(self, name):
        matchingFilePaths = []
        openFolders = self.view.window().folders()
        if len(openFolders) == 1:
            baseDir = os.path.abspath(openFolders[0])
            srcDirPath = os.path.join(baseDir, "src")
            if os.path.isdir(srcDirPath):
                subdirDict = dict({
                    "classes": "cls", 
                    "pages": "page"
                })
                for subdir in os.listdir(srcDirPath):
                    fullPath = os.path.join(srcDirPath, subdir)
                    if os.path.isdir(fullPath) and subdir in subdirDict:
                        fileNameToSearchFor = os.path.join(fullPath, name + "." + subdirDict[subdir])
                        print("Searching for " + fileNameToSearchFor)
                        if(os.path.lexists(fileNameToSearchFor)):
                            matchingFilePaths.append(fileNameToSearchFor)
            else:
                print("Error: Current folder doesn't appear to be a MavensMate directory (failed to find 'src' subdirectory)")
        else:
            print("Error: More than one folder currently open")
        return matchingFilePaths

