from Individual import  Individual


class Population:

    def __init__(self, tsp, len):
        # size of tours
        self.len = len
        self.dimension = tsp.DIMENSION

        self.tsp = tsp

        # list of tours
        self.tourlist = []

    # initial the tourlist
    def ini_tourlist(self):
        for i in range(self.len):
            ind = Individual(self.tsp)
            self.tourlist.append(ind)

    # for all individual, set the length of each individual
    def set_length(self):
        for individual in self.tourlist:
            individual.calDis()

    # for all individual, set the adaptability of each individual
    def set_adaptability(self):
        for individual in self.tourlist:
            individual.adaptability = 1 / individual.length
