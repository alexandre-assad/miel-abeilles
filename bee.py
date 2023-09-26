import random
import time
from utils.math_utils import manhattan_distance

class Bee:

    def __init__(self,flowers=[]):
        self.genetics = flowers #Will be list of flowers traveled through
        self.score = self.fitness_score([500,500]) #Will be the fitness score


    def fitness_score(self,departure:list) ->int:
        """
        Input : coordinates : coords of departures
        Output : a manathan distance of the travel
        """
        if self.genetics == []:
            return 0
        
        distance = manhattan_distance(departure,self.genetics[0]) + manhattan_distance(departure,self.genetics[-1])
        for i in range(len(self.genetics)-1):
            distance += manhattan_distance(self.genetics[i],self.genetics[i+1])
        return distance
