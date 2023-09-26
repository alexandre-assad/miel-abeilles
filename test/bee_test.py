from bee import Bee
import unittest

class TestBee(unittest.TestCase):

    def setUp(self) -> None:
        self.bee1 = Bee()
        return super().setUp()
    

    def test_random_travel(self):
        coords_test = [[1,4],[2,7]]
        self.bee1.random_travel(coords_test)
        self.assertEqual(len(self.bee1.genetics),2)
        self.assertEqual(self.bee1.genetics[0] in coords_test,True)

    def test_fitness_score(self):
        coords_test = [[200,600],[400,400],[600,500]]
        self.assertEqual(self.bee1.fitness_score([500,500],coords_test) in [1200,1400],True)