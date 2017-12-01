import unittest
from xlearn3.model import modelInfoReader
import xlearn3
import tensorflow as tf
import numpy as np

class TestMnistModel(unittest.TestCase):
    modelPath = "testdata/mnist_cnn"


    def initModel(self):
        np.random.seed(10)
        tf.set_random_seed(10)
        modelPath = "%s/%s" % (xlearn3.__path__[0], self.modelPath)
        mI = modelInfoReader.ModelInfo(modelPath)
        self.model = mI.model

    # def test_training_model(self):
    #     assert self.model.canTrain() == False

    def initBatch(self):
        self.x = np.array(np.random.random((10,28,28,3)), dtype=np.float32)
        self.y = np.array(np.eye(10), dtype=np.float32)

    def test_computing_loss(self):
        self.initModel()
        self.initBatch()
        sess = tf.Session()
        tf.global_variables_initializer().run(session=sess)
        
        for i in range(30):
            feedDict = {self.model.x: self.x, self.model.y: self.y, self.model.keep_prob: 1}
            loss = self.model.loss.eval(feedDict, session=sess)
            print "Loss at Step no. %d is %f" % (i,loss) 
            self.model.optimizer.run(feedDict, session=sess)





if __name__ == '__main__':
    unittest.main()
