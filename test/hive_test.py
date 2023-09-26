from hive import Hive
from bee import Bee
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
        self.assertNotEqual(self.hive1.bees[0],self.hive1.bees[5])
        self.hive1.genetics_algorythm()
        self.assertEqual(len(self.hive1.bees),100)
        self.assertEqual(self.hive1.bees[0].genetics,self.hive1.bees[5].genetics)

    def test_reproduction(self):
        bee1,bee2 = Bee(), Bee()
        bee1.genetics,bee2.genetics = [[200,600],[400,400],[600,500]], [[400,400],[600,500],[200,600]]
        bee1.score,bee2.score = bee1.fitness_score([500,500]),bee2.fitness_score([500,500])
        bees_new = self.hive1.reproduction(bee1,bee2)
        self.assertEqual(bees_new[1].genetics,[[200,600],[400,400],[600,500]])
