from utils.pandas_utils import coordinates_scrap
from bee import Bee
import random
import math

class Hive:


    def __init__(self):
        self.flowers = coordinates_scrap() #Will scap flowers_coordinates csv
        self.bees = []
        for i in range(100):
            #random.shuffle(self.flowers)
            flowers = sorted(self.flowers, key=lambda x: random.random())
            self.bees.append(Bee(flowers))



    def get_mean_score(self):
        return (sum(self.bees[i].score for i in range(len(self.bees))))/len(self.bees)
    
    def genetics_algorythm(self):
        """
        Basic code : Genetics algorythm like: a 1st generation, then natural selection, reproduction with the 50 best bees with the death of the 50 worst, then continue and add some mutations sometimes
        """
        run = True
        countdown = 0
        min_average_score = math.inf
        while run:
            self.bees.sort(key=self.get_score)
            del self.bees[50:]

            average_score = self.get_mean_score()
            if average_score <= min_average_score +10 and average_score >= min_average_score-10:

                self.bees[random.randint(1,49)].mutation()
                self.bees[random.randint(1,49)].mutation()
                self.bees[random.randint(1,49)].mutation()
                countdown += 1

            elif average_score < min_average_score:
                min_average_score = average_score

            for i in range(0,49,2):
                self.reproduction(self.bees[i],self.bees[i+1])
            

            if countdown == 1000:
                run = False
            
            

            
    


        
    def reproduction(self,bee1:Bee,bee2:Bee) ->list[Bee]:
        """
        Input : two bees
        Basic Code : make a reproduction of two bees, which takes one chromosom by two of parent's ones.
        Output : a list of two new bees
        """
        self.bees.append(self.baby(bee1,bee2,"first"))
        self.bees.append(self.baby(bee1,bee2,"second"))



    def baby(self,parent1:Bee,parent2:Bee,state:str) -> Bee:
        if state == "first":
            genetic1 = parent1.genetics.copy()
            genetic2 = parent2.genetics.copy()
            baby_bee = Bee()
            baby_bee.genetics = []

            while len(genetic1) > 0:
                gene1 = genetic1[0]
                baby_bee.genetics.append(gene1)
                genetic1.remove(gene1)
                genetic2.remove(gene1)
                if len(genetic2) == 0:
                    baby_bee.score = baby_bee.fitness_score([500,500])
                    return baby_bee
                gene2 = genetic2[0]
                baby_bee.genetics.append(gene2)
                genetic1.remove(gene2)
                genetic2.remove(gene2)
            baby_bee.score = baby_bee.fitness_score([500,500])
            return baby_bee
        
        elif state == "second":
            genetic1 = parent1.genetics.copy()
            genetic2 = parent2.genetics.copy()
            baby_bee = Bee()
            baby_bee.genetics = []

            while len(genetic2) > 0:
                gene1 = genetic2[0]
                baby_bee.genetics.append(gene1)
                genetic2.remove(gene1)
                genetic1.remove(gene1)
                if len(genetic1) == 0:
                    baby_bee.score = baby_bee.fitness_score([500,500])
                    return baby_bee
                gene2 = genetic1[0]
                baby_bee.genetics.append(gene2)
                genetic2.remove(gene2)
                genetic1.remove(gene2)
            baby_bee.score = baby_bee.fitness_score([500,500])
            return baby_bee


    def get_score(self,bee):
        return bee.score
    