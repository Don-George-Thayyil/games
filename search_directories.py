import os

class SearchDirectory:
    def find_dir(self,path,dir):
        try:
            os.chdir(path)
        except OSError:
            print("Path not found")
            return
        curr = os.getcwd()
        for item in os.listdir("."):
            if item == dir:
                print(os.getcwd() + '/' + dir)
            self.find_dir(curr + "/" + item, dir)
                
obj = SearchDirectory()
obj.find_dir("./somefolder","findme")