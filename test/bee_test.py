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
        self.bee1.genetics = coords_test
        self.assertEqual(self.bee1.fitness_score([500,500]) in [1200,1400],True)

    def test_mutation(self):
        coord_test = [[1,2],[3,4],[4,5]]
        self.bee1.genetics = coord_test
        self.bee1.mutation()
        self.assertEqual(len(self.bee1.genetics),3)
        self.assertNotEqual(self.bee1.genetics, [[1,2],[3,4],[4,5]])