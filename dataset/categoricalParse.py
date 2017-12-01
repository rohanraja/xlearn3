import numpy as np
from BaseParser import BaseParser
from xlearn3.utils import utils

class CategoricalParser(BaseParser):


    outP = []

    def parse(self):
        if(len(self.outP) != 0):
            return self.outP

        self.outP = np.array(self.rowList, dtype=int)
        return self.outP

    def GetSlice(self, st, end):

        allList = self.parse()
        return utils.dense_to_one_hot(allList[st:end])
