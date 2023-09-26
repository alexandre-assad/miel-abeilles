from hive import Hive
import unittest

class TestHive(unittest.TestCase):

    def setUp(self) -> None:
        self.hive1 = Hive()
        return super().setUp()
    
    def test_init(self):
        self.assertEqual(self.hive1.pos,[500,500])
        self.assertEqual(len(self.hive1.bees),100)
        self.assertEqual(len(self.hive1.flowers),50)