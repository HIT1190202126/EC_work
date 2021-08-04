import random
import Individual
import TSPProblem


class Mutation:
    """
    The Class deal with mutation
    """

    def __init__(self, size, tspproblem):
        """
        Constructor
        :param size :
        :param tsp :A tspproblem object
        """
        self.size = size
        self.dim = tspproblem.DIMENSION
        self.tspp = tspproblem

    def getRand2(self):
        """
        Helper function
        get 2 randomly choose index
        :return: idx1,idx2 two index in range [0,self.dim-1](idx1 < idx2)
        """
        idx1 = 0
        idx2 = 0
        while idx2 == idx1:
            idx1 = random.randint(0, self.dim - 1)
            idx2 = random.randint(0, self.dim - 1)
        if idx1 > idx2:
            t = idx2
            idx2 = idx1
            idx1 = t

        # print(idx1," ",idx2)
        return idx1, idx2

    def swapMutation(self, ind):
        """
        Use swap to Mutate a new solution
        :param ind:an individual object
        :return:The SAME individual object which has been Mutated
        """
        idx1, idx2 = self.getRand2()
        # swap
        t = ind.tour[idx1]
        ind.tour[idx1] = ind.tour[idx2]
        ind.tour[idx2] = t
        return ind

    def insertMutation(self, ind):
        """
        Use insertion to Mutate a new solution
        :param ind: an individual object
        :return: The SAME individual object which has been Mutated
        """
        idx1, idx2 = self.getRand2()
        ind.tour.insert(idx1 + 1, ind.tour[idx2])
        ind.tour.pop(idx2 + 1)
        return ind

    def invertionMutation(self, ind):
        """
        Use invertion to Mutate a new solution
        :param ind: an individual object
        :return: The SAME individual object which has been Mutated
        """
        idx1, idx2 = self.getRand2()
        subList = ind.tour[idx1:idx2]
        subList.reverse()
        ind.tour[idx1:idx2] = subList
        return ind

    def scrambleMutation(self, ind):
        """
        Use scramble to Mutate a new solution
        :param ind: an individual object
        :return: The SAME individual object which has been Mutated
        """
        idx1, idx2 = self.getRand2()
        subList = ind.tour[idx1:idx2]
        random.shuffle(subList)
        ind.tour[idx1:idx2] = subList
        return ind


# Testing Correctness

if __name__ == "__main__":
    location1 = "dataSet/eil51.tsp/eil51.tsp"
    location2 = "dataSet/eil51.opt.tour/eil51.opt.tour"
    TSP0 = TSPProblem.TSPProblem(location1, location2)
    Ind = Individual.Individual(TSP0)
    Ind.RandomTour()
    print(Ind.tour)
    Ind = Mutation(0, TSP0).swapMutation(Ind)
    print("After SWAP", Ind.tour)
    Ind = Mutation(0, TSP0).insertMutation(Ind)
    print("After Insert", Ind.tour)
    Ind = Mutation(0, TSP0).scrambleMutation(Ind)
    print("After scramble", Ind.tour)
    Ind = Mutation(0, TSP0).invertionMutation(Ind)
    print("After invert", Ind.tour)
