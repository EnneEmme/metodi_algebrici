import unittest

from utils import *
from methods import *

class TestEuclideanAlgorithm(unittest.TestCase):

    def test_euclidean_algorithm1(self):
        a, b = 819, 315
        MCD, _ = euclidean_algorithm(a, b, False)

        self.assertEqual(MCD, gcd(a, b))


if __name__ == '__main__':
    unittest.main()
