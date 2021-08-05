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
            ind.RandomTour()
            self.tourlist.append(ind)

    # for all individual, set the length of each individual
    def set_length(self):
        for individual in self.tourlist:
            individual.calDis()

    # for all individual, set the adaptability of each individual
    def set_adaptability(self):
        # compute adaptability and normalization(0 - 1 float,bigger is better)
        ind_list = self.tourlist
        a = []
        min = ind_list[0].length
        max = min
        for ind in ind_list:
            tmp = ind.length
            a.append(tmp)
            if (tmp < min):
                min = tmp
            if (tmp > max):
                max = tmp
            ind.adaptability = tmp
        for ind in ind_list:
            if (max != min):
                ind.adaptability = 1 - ind.length / max
            else:
                ind.adaptability = 0.5
