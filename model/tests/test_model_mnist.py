import unittest
from xlearn3.model import modelInfoReader
from xlearn3.dataset import datasetReader
import xlearn3
import tensorflow as tf
import numpy as np
from itertools import cycle


class TestMnistModel(unittest.TestCase):
    modelPath = "testdata/mnist_cnn"
    datasetPath = "testdata/dataset/mnist_png"


    def initDataset(self):
        jsonPath = "%s/%s" % (xlearn3.__path__[0], self.datasetPath)
        self.dsinfo = datasetReader.DataSetInfo(jsonPath)
        assert self.dsinfo.Count == 70000

    def initModel(self):
        tf.reset_default_graph()
        np.random.seed(10)
        tf.set_random_seed(10)
        modelPath = "%s/%s" % (xlearn3.__path__[0], self.modelPath)
        mI = modelInfoReader.ModelInfo(modelPath)
        self.model = mI.model

    # def test_training_model(self):
    #     assert self.model.canTrain() == False

    bgen = None
    def initBatch(self):

        if self.bgen == None:
            batchSize = 64
            self.bgen = cycle(self.dsinfo.getBatchGen(batchSize))
        x,y = next(self.bgen)
        self.x = x[0]
        self.y = y[0]


    def test_training_mnist(self):
        self.initDataset()
        self.initModel()
        sess = tf.Session()
        tf.global_variables_initializer().run(session=sess)
        
        self.initBatch()
        feedDict = {self.model.x: self.x, self.model.y: self.y, self.model.keep_prob: 0.1}
        initLoss = self.model.loss.eval(feedDict, session=sess)
        loss = 10000000

        for i in range(3):
            self.initBatch()
            feedDict = {self.model.x: self.x, self.model.y: self.y, self.model.keep_prob: 0.4}
            feedDictPred = {self.model.x: self.x, self.model.keep_prob: 1}
            loss = self.model.loss.eval(feedDict, session=sess)
            print("Loss at Step no. %d is %f" % (i,loss)) 
            self.model.optimizer.run(feedDict, session=sess)
            print("Accuracy: " , self.model.accuracy.eval(feedDict, session=sess))
            # print self.model.correct_prediction.eval(feedDict, session=sess)
            # print self.model.pred.eval(feedDictPred, session=sess)

        sess.close()

        # assert loss < initLoss





if __name__ == '__main__':
    unittest.main()
