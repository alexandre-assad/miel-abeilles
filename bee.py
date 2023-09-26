import random
from utils.math_utils import manhattan_distance

class Bee:

    def __init__(self):
        self.genetics = [] #Will be list of flowers traveled through
        self.score = 0 #Will be the fitness score

    def random_travel(self,flowers:list) ->None:
        """
        Input : a list of list of int, a list of coordinates x and y
        Output : no output, the input list shuffle into self.genetics
        """
        random.shuffle(flowers)
        self.genetics = flowers


    def fitness_score(departure:list,flowers:list) ->int:
        """
        Input : coordinates : coords of departures and coords of flowers
        Output : a manathan distance of the travel
        """
        pass