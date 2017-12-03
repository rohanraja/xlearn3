import unittest
from xlearn3.utils import utils
import numpy as np

class TestDenseToOneHot(unittest.TestCase):

    def test_dense_to_one_hot(self):
        print(utils.dense_to_one_hot(np.array([1,2,3,9]), 10))

if __name__ == '__main__':
    unittest.main()
