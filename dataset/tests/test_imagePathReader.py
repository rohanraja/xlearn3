import unittest
from xlearn3.dataset import imagePathReader
import xlearn3

class TestImagePathParser(unittest.TestCase):
    def test_parse(self):

        imgPath = "%s/%s" % (xlearn3.__path__[0], "testdata/dataset/googlelogo_color_120x44dp.png")
        parsr = imagePathReader.ImagePathParser([imgPath], {})
        outp = parsr.parse()
        print(outp.shape)
        assert outp.shape[3] == 1


if __name__ == '__main__':
    unittest.main()
