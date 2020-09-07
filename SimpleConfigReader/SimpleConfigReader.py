"""
https://github.com/DaemonAeon/SimpleConfigReader
"""
class SimpleConfigReader:
    def __init__(self, file):
        self.file = file

    def get(self, key):
        f = open(self.file, "r")
        for line in f:
            lineAsList = line.split("=")
            if lineAsList[0] == key:
                return lineAsList[1]
        f.close()
        raise NameError('Key not found in file ' + self.file)