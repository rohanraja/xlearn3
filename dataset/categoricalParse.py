import numpy as np
from BaseParser import BaseParser
from xlearn3.utils import utils

class CategoricalParser(BaseParser):


    outP = []


    def parse(self):
        if(len(self.outP) != 0):
            return self.outP


        try:
            self.outP = np.array(self.rowList, dtype=int)
            return self.outP
        except:
            rowsOut = []
            rowCatsDict = {}
            for row in self.rowList:
                
                if row not in rowCatsDict:
                    rowCatsDict[row] = len(rowCatsDict) + 1

                rownum = rowCatsDict[row] - 1
                rowsOut.append(rownum)

            self.outP = np.array(rowsOut, dtype=int)
            return self.outP

    def GetSlice(self, st, end):

        allList = self.parse()
        return utils.dense_to_one_hot(allList[st:end])
