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


    def fitness_score(self,departure:list) ->int:
        """
        Input : coordinates : coords of departures
        Output : a manathan distance of the travel
        """
        distance = manhattan_distance(departure,self.genetics[0]) + manhattan_distance(departure,self.genetics[-1])
        for i in range(len(self.genetics)-1):
            distance += manhattan_distance(self.genetics[i],self.genetics[i+1])
        return distance