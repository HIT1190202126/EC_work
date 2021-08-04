import random
import numpy as np
import math


class Individual:
    def __init__(self, tsp):
        # set parameters
        self.dimension = tsp.DIMENSION
        self.pos = tsp.POS
        self.tour = []
        self.length = 0
        self.adaptability = 0

    # for comparation
    def __lt__(self, other):
        return True if self.adaptability < other.adaptability else False


    def calDis(self):
        """
        Get the length of this individual
        """
        self.length = 0
        for i in range(self.dimension - 1):
            cityone = self.pos[int(self.tour[i]) - 1]
            citytwo = self.pos[int(self.tour[i + 1]) - 1]
            x1 = cityone[1]
            y1 = cityone[2]
            x2 = citytwo[1]
            y2 = citytwo[2]
            self.length = self.length + math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def calDis2(self,city1,city2):
        """
        return math.sqrt((city1[1] - city2[1]) * (city1[1] - city2[1]) + (city1[2] - city2[2]) * (city1[2
        :param city1:
        :param city2:
        :return:
        """
        return math.sqrt((city1[1]-city2[1])*(city1[1]-city2[1])+(city1[2]-city2[2])*(city1[2]-city2[2]))
    # construct a random array in O(n)
    def RandomTour(self):
        LastPos = random.randint(0, self.dimension - 1)
        self.tour.append(LastPos)
        while len(self.tour) != self.dimension:
            NextPos = random.randint(0, self.dimension - 1)
            if NextPos not in self.tour:
                self.tour.append(NextPos)
                self.length = self.length + self.calDis2(self.pos[LastPos], self.pos[NextPos])
            LastPos = NextPos

    # find index by city,根据值找到对应的下标 value->key
    def find_index(self, city):
        for i in range(0, len(self.tour)):
            if city == self.tour[i]:
                return i
