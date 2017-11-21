class BaseParser:

    def __init__(self, rowList, colInfo):
        self.rowList = rowList
        self.colInfo = colInfo

    def GetSlice(self, st, end):

        allList = self.parse()

        return allList[st:end]
