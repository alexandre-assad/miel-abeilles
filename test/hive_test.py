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

    def test_genetics_algorythm(self):
        self.hive1.genetics_algorythm()
        self.assertEqual(len(self.hive1.bees),100)
        self.assertEqual(self.hive1.bees[2].genetics,self.hive1.bees[31].genetics)