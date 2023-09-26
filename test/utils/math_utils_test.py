from utils.math_utils import *
import unittest

class TestMathUtils(unittest.TestCase):

    def test_manhattan_distance(self):
        pos1, pos2 = [500,500],[200,600]
        self.assertEqual(manhattan_distance(pos1,pos2),400)