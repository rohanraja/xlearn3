import numpy as np
from BaseParser import BaseParser

class CategoricalParser(BaseParser):


    def parse(self):
        return np.array(self.rowList)
