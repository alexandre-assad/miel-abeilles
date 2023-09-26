from utils.pandas_utils import coordinates_scrap
from bee import Bee

class Hive:


    def __init__(self):
        self.pos = [500,500]
        self.flowers = coordinates_scrap() #Will scap flowers_coordinates csv
        self.bees = [Bee(self.flowers) for i in range(100)] #will be a list of 100 bees


    def selection_best_travel(self) ->list:
        return self.bees.sort(key=self.get_score)

    def get_score(self):
        return self.bees.score
    
    def genetics_algorythm(self):
        """
        Basic code : Genetics algorythm like: a 1st generation, then natural selection, reproduction with the 50 best bees with the death of the 50 worst, then continue and add some mutations sometimes
        """
        run = True
        while run:
            self.bees = self.selection_best_travel(self.bees)
            self.bees = self.bees[:50]
            if self.bees[0].score == self.bees[49].score and self.bees[0].score == self.bees[30].score:
                run = False
            for i in range(0,49,2):
                bees_newborn = self.reproduction(self.bees[0],self.bees[1])
                self.bees.append(bees_newborn[0])
                self.bees.append(bees_newborn[1])

        
    def reproduction(self,bee1:Bee,bee2:Bee) ->list[Bee]:
        genetic1, genetic2 = bee1.genetics.copy(),bee2.genetics.copy()
        new_born = []
        new_bee1,new_bee2 = Bee(),Bee()
        while len(genetic1) >0:
            new_bee1.genetics.append(genetic1[0])
            genetic2.remove(genetic1[0])
            genetic1.remove(genetic1[0])
            if len(genetic2) == 0:
                break
            new_bee1.genetics.append(genetic2[0])
            genetic1.remove(genetic2[0])
            genetic2.remove(genetic2[0])
        new_born.append(new_bee1)
        genetic1, genetic2 = bee1.genetics.copy(),bee2.genetics.copy()
        while len(genetic2) >0:
            new_bee2.genetics.append(genetic2[0])
            genetic1.remove(genetic2[0])
            genetic2.remove(genetic2[0])
            if len(genetic1) == 0:
                break
            new_bee2.genetics.append(genetic1[0])
            genetic2.remove(genetic1[0])
            genetic1.remove(genetic1[0])
            
        new_born.append(new_bee2)
        return new_born
            