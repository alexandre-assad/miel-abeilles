from utils.os_utils import *
import unittest

class TestOsUtils(unittest.TestCase):

    def test_path_coordinates(self):
        self.assertEqual(path_coordinates("flowers_coordinates.csv"),"coordinates/flowers_coordinates.csv")