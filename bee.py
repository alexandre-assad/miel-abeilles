import random
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

    def mutation(self):
        if len(self.genetics) <=1:
            return self.genetics
        else:
            random_1 = random.randint(0,len(self.genetics)-1)
            while True:
                random_2 = random.randint(0,len(self.genetics)-1)
                if random_2 != random_1:
                    break
            gene1 = self.genetics[random_1]
            gene2 = self.genetics[random_2]
            self.genetics[random_1] = gene2
            self.genetics[random_2] = gene1
        self.score = self.fitness_score([500,500])