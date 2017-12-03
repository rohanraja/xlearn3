class BaseTensorflow:

    def processBatch(self, batch):
        self.xVal = []
        self.yVal = []
        feedDict = {self.x: self.xVal, self.model.y: self.yVal, self.model.keep_prob: 1}
        return feedDict

    def train_batchGen(self, batchGen, nEpochs, params={}):

        for i in range(nEpochs):
            for batch in batchGen:
                feedDict = self.processBatch(batch)
                loss = self.loss.eval(feedDict, session=self.sess)
                print "Loss at Step no. %d is %f" % (i,loss) 
                self.optimizer.run(feedDict, session=self.sess)


