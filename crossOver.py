import Individual
import TSPProblem
import random


class crossOver:
    def __init__(self, size, tsp):
        self.tsp = tsp
        self.dimension = tsp.DIMENSION
        self.size = size

    def cycle_crossover(self, parent1, parent2):
        # init child
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)
        child1.tour = parent2
        child2.tour = parent1

        # init
        start_pos = random.randint(0, self.dimension - 1)
        start = parent1.tour[start_pos]
        next = parent2.tour[start_pos]
        cur_pos = start_pos
        cy = []
        cy.append(cur_pos)
        # Make a cycle
        while next != start:
            cur_pos = parent1.find_index(next)
            cy.append(cur_pos)
            next = parent2.tour[cur_pos]

        # CrossOver
        for i in range(len(cy)):
            child1.tour[cy[i]] = parent1.tour[cy[i]]
            child2.tour[cy[i]] = parent2.tour[cy[i]]
        return child1, child2

    def order_crossover(self, parent1, parent2):
        # init child
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)

        # randomly choose a part from parent
        startgene = random.randin(0, self.dimension - 2)
        endgene = random.randint(startgene + 1, self.dimension - 1)

        # Copy process
        # Child1
        i = 0
        gene1 = parent1.tour[startgene: endgene]
        while len(child1.tour) < startgene:
            if parent2.tour[i] not in gene1:
                child1.tour.append(parent2.tour[i])
            i = i + 1

        for cnt in range(endgene - startgene + 1):
            child1.tour.append(gene1[cnt])

        while len(child1.tour) < self.dimension:
            if parent2.tour[i] not in gene1:
                child1.tour.append(parent2.tour[i])
            i = i + 1

        # Child2
        i = 0
        gene2 = parent2.tour[startgene: endgene]
        while len(child2.tour) < startgene:
            if parent1.tour[i] not in gene2:
                child2.tour.append(parent1.tour[i])
            i = i + 1

        for cnt in range(endgene - startgene + 1):
            child2.tour.append(gene2[cnt])

        while len(child2.tour) < self.dimension:
            if parent1.tour[i] not in gene2:
                child2.tour.append(parent1.tour[i])
            i = i + 1

        return child1, child2

    def PMX_crossover(self, parent1, parent2):
        # init child
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)
        child1.tour = parent1.tour
        child2.tour = parent2.tour
        # randomly choose a part from parent
        startgene = random.randint(0, self.dimension - 2)
        endgene = random.randint(startgene + 1, self.dimension - 1)
        gene1 = parent1.tour[startgene: endgene + 1]
        gene2 = parent2.tour[startgene: endgene + 1]
        # 冲突检测 check if there is a conflict,建立一个映射
        dic1 = {}
        dic2 = {}
        for i in range(endgene - startgene + 1):
            dic1[gene2[i]] = gene1[i]
            dic2[gene1[i]] = gene2[i]
        # copy
        child1.tour[startgene: endgene + 1] = gene2
        child2.tour[startgene: endgene + 1] = gene1
        # 根据映射调整基因
        # Child1
        for i in range(startgene):
            while child1.tour[i] in dic1.keys():
                child1.tour[i] = dic1[child1.tour[i]]

        for i in range(endgene + 1, self.dimension):
            while child1.tour[i] in dic1.keys():
                child1.tour[i] = dic1[child1.tour[i]]
        # Child2
        for i in range(startgene):
            while child2.tour[i] in dic2.keys():
                child2.tour[i] = dic2[child2.tour[i]]

        for i in range(endgene + 1, self.dimension):
            while child2.tour[i] in dic2.keys():
                child2.tour[i] = dic2[child2.tour[i]]

        return child1, child2
