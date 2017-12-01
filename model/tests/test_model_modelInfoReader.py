import unittest
from xlearn3.model import modelInfoReader
import xlearn3
import tensorflow as tf

class TestModelInfo(unittest.TestCase):
    pyPath = "testdata/model1"
    modelPath = "testdata/mnist_cnn"

    def test_model_info(self):
        tf.reset_default_graph()
        modelPath = "%s/%s" % (xlearn3.__path__[0], self.modelPath)
        mI = modelInfoReader.ModelInfo(modelPath)
        assert mI.model.canTrain() == False

    def test_importing_model_file(s):
        pyPath = "%s/%s" % (xlearn3.__path__[0], "testdata/model1")
        pyName = "mymodel"
        clsName = "MyModel"
        Cls = modelInfoReader.readClassFromPyFile(pyPath, pyName, clsName)
        obj = Cls()
        assert obj.canTrain() == False


if __name__ == '__main__':
    unittest.main()
