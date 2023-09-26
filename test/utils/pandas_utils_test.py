import unittest

from utils.pandas_utils import *

class TestPandasUtils(unittest.TestCase):

    def test_coordinates_scrap(self):
        flowers = coordinates_scrap()
        self.assertEqual(flowers[0],[796,310])
        self.assertEqual(flowers[1][1],130)
