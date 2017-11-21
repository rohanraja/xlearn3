import unittest
from xlearn3.dataset import imagePathReader

class TestImagePathParser(unittest.TestCase):
    def test_parse(self):

        parsr = imagePathReader.ImagePathParser(["tests/data/googlelogo_color_120x44dp.png"], {})
        outp = parsr.parse()
        print outp.shape
        assert outp.shape[3] == 3


if __name__ == '__main__':
    unittest.main()
