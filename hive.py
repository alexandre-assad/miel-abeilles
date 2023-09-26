from utils.pandas_utils import coordinates_scrap
from bee import Bee

class Hive:


    def __init__(self):
        self.pos = [500,500]
        self.flowers = coordinates_scrap() #Will scap flowers_coordinates csv
        self.bees = [Bee(self.flowers) for i in range(100)] #will be a list of 100 bees



    
    def genetics_algorythm(self):
        """
        Basic code : Genetics algorythm like: a 1st generation, then natural selection, reproduction with the 50 best bees with the death of the 50 worst, then continue and add some mutations sometimes
        """
        run = True
        while run:
            self.bees.sort(key=self.get_score)
            self.bees = self.bees[:50]
            if self.bees[0].score == self.bees[49].score and self.bees[0].score == self.bees[30].score:
                run = False
            for i in range(0,50,2):
                bees_newborn = self.reproduction(self.bees[i],self.bees[i+1])
                self.bees.append(bees_newborn[0])
                self.bees.append(bees_newborn[1])
            

        
    def reproduction(self,bee1:Bee,bee2:Bee) ->list[Bee]:
        """
        Input : two bees
        Basic Code : make a reproduction of two bees, which takes one chromosom by two of parent's ones.
        Output : a list of two new bees
        """
        genetic1, genetic2 = bee1.genetics.copy(),bee2.genetics.copy()
        new_born = []
        new_bee1,new_bee2 = Bee(),Bee()
        while genetic1 != []:
            gen1 = genetic1[0]
            new_bee1.genetics.append(gen1)
            genetic1.remove(gen1)
            genetic2.remove(gen1)
            if genetic2 == []:
                break
            gen2 = genetic2[0]
            new_bee1.genetics.append(gen2)
            genetic2.remove(gen2)
            genetic1.remove(gen2)
        new_bee1.score = new_bee1.fitness_score([500,500])
        new_born.append(new_bee1)
        while genetic2 != []:
            gen1 = genetic2[0]
            new_bee2.genetics.append(gen1)
            genetic1.remove(gen1)
            genetic2.remove(gen1)
            if genetic1 == []:
                break
            gen2 = genetic1[0]
            new_bee2.genetics.append(gen2)
            genetic2.remove(gen2)
            genetic1.remove(gen2)
        new_bee2.score = new_bee2.fitness_score([500,500])
        new_born.append(new_bee2)
        return new_born

    def get_score(self,bee):
        return bee.score
    