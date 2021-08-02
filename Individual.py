
import random
import numpy as np
import math

class Individual:
    def __init__(self,tsp):
        #set parameters
        self.dimension = tsp.DIMENSION
        self.pos = tsp.POS
        self.tour = []
        self.length = 0
        self.adaptability = 0
    #for comparation
    def __lt__(self,other):
        return True if self.adaptability < other.adaptability else False
    #calculate distance
    def calDis(city1,city2):
        return math.sqrt((city1[1]-city2[1])*(city1[1]-city2[1])+(city1[2]-city2[2])*(city1[2]-city2[2]))
    #construct a random array in O(n)
    def RandomTour(self):
        LastPos = random.randint(0, self.dimension-1)
        self.tour.append(LastPos)
        while len(self.tour) != self.dimension:
            NextPos = random.randint(0, self.dimension-1)
            if NextPos not in self.tour:
                self.tour.append(NextPos)
                self.length = self.length + calDis(self.pos[LastPos],self.pos[NextPos])

    
