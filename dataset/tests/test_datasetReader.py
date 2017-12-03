import unittest
from xlearn3.dataset import datasetReader
import xlearn3

class TestDataSetInfo(unittest.TestCase):

    doneSetup = False

    def setUp(self):
        if self.doneSetup == True:
            return
        self.doneSetup = True
        jsonPath = "%s/%s" % (xlearn3.__path__[0], "testdata/dataset")
        self.dsinfo = datasetReader.DataSetInfo(jsonPath)

    def test_json_loading(self):

        assert self.dsinfo.X.index("filePath") != -1

    def test_CSV_Loading_Count(self):

        assert self.dsinfo.Count == 79

    def test_getBatchGen(self):

        bgen = self.dsinfo.getBatchGen(10)

        x,y = next(bgen)

        assert len(y[0]) == 10 # TODO: implement your test here

    def test_getBatchGenLastLen(self):

        batchSize = 10
        bgen = self.dsinfo.getBatchGen(batchSize)

        lastLen = 0
        numBatches = 0
        for x,y in bgen:
            lastLen = len(y[0])
            numBatches += 1

        assert lastLen == self.dsinfo.Count % batchSize
        assert numBatches == 8



if __name__ == '__main__':
    unittest.main()
