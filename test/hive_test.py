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
        self.assertNotEqual(self.hive1.bees[0].genetics,self.hive1.bees[97].genetics)

    def test_genetics_algorythm(self):
        
        self.assertNotEqual(self.hive1.bees[0].genetics,self.hive1.bees[97].genetics)
        self.hive1.genetics_algorythm()
        self.assertEqual(len(self.hive1.bees),100)
        self.assertEqual(len(self.hive1.bees[51].genetics),50)


    def test_reproduction(self):
        bee1,bee2 = Bee(), Bee()
        bee1.genetics,bee2.genetics = [[200,600],[400,400],[600,500]], [[400,400],[600,500],[200,600]]
        bee1.score,bee2.score = bee1.fitness_score([500,500]),bee2.fitness_score([500,500])
        self.hive1.bees = [bee1,bee2]
        self.assertEqual(len(self.hive1.bees),2)
        self.hive1.reproduction(bee1,bee2)
        self.assertEqual(len(self.hive1.bees),4)
        self.assertEqual(self.hive1.bees[3].genetics,[[400,400],[200,600],[600,500]])
        
