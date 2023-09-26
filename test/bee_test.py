from bee import Bee
import unittest

class TestBee(unittest.TestCase):

    def setUp(self) -> None:
        self.bee1 = Bee()
        return super().setUp()
    

    def test_travel(self):
        coords_test = [[1,4],[2,7]]
        self.bee1.travel(coords_test)
        self.assertEqual(len(self.bee1.genetics),2)
        self.assertEqual(self.bee1.genetics[0] in coords_test,True)