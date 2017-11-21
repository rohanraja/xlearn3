import cv2
import numpy as np
from BaseParser import BaseParser


class ImagePathParser(BaseParser):


    outP = []

    def readImage(self, imgFile):
        image = cv2.imread(imgFile)
        return image

    def parse(self):

        if(len(self.outP) != 0):
            return self.outP

        outP = []

        for imgP in self.rowList:
            outP.append(self.readImage(imgP))

        self.outP = np.array(outP)
        return self.outP



if __name__ == "__main__":

    parsr = ImagePathParser(["/Volumes/Fireice/Users/rraja/code/dataset/cat/googlelogo_color_120x44dp.png"], {})
    outp = parsr.parse()
    print outp.shape
