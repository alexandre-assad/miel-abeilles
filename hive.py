from utils.pandas_utils import coordinates_scrap
from bee import Bee

class Hive:


    def __init__(self):
        self.pos = [500,500]
        self.flowers = coordinates_scrap() #Will scap flowers_coordinates csv
        self.bees = [Bee(self.flowers) for i in range(100)] #will be a list of 100 bees

    
    def genetics_algorythm(self):
        pass