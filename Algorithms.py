from os import path
import random
import crossOver
import Selection
import mutation
from Population import Population
from Individual import Individual
from TSPProblem import TSPProblem
from Selection import Selection
from crossOver import crossOver
from mutation import Mutation

"""
pmx_crossover+swap_mutation+tournament_selection
population_size: number of individuals
tsp_path: the path which points to the .tsp file
opt_path: the path which points to the .Opt file
batch_size: number of generations
"""

# 进行一次独立的训练
def EA1(population_size, tsp_path, opt_path, batch_size):
    mutation_possibility = 6
    tsp = TSPProblem(tsp_path, opt_path)
    pop = Population(tsp, population_size)
    # initial
    pop.ini_tourlist()

    pop.set_length()
    pop.set_adaptability()

    log_tour = []
    log_len = []

    for i in range(batch_size):
        # optimize 1/3 parents
        t = pop.len
        parents_pop = Selection().tournament_selection(int(pop.len / 3), 3, tsp, t, pop)

        # cross random from parents
        child_list = []
        while len(child_list) != population_size:
            pa1 = random.randint(0, parents_pop.len - 1)
            pa2 = random.randint(0, parents_pop.len - 1)
            pa1 = parents_pop.tourlist[pa1]
            pa2 = parents_pop.tourlist[pa2]

            # cross
            ch1, ch2 = crossOver(size=0, tsp=tsp).PMX_crossover(pa1, pa2)
            child_list.append(ch1)
            child_list.append(ch2)

        for j in range(population_size):
            rate = random.randint(1, 10)
            # mutation
            if rate <= mutation_possibility:
                child_list[j] = Mutation(size=0, tspproblem=tsp).swapMutation(child_list[j])

        # make the child population
        pop = Population(tsp, population_size)
        pop.tourlist = child_list
        pop.set_length()
        pop.set_adaptability()

        if i % 100 == 0:
            min_len = pop.tourlist[0].length
            min_index = 0
            for j in range(1, pop.len):
                if pop.tourlist[j].length < min_len:
                    min_len = pop.tourlist[j].length
                    min_index = j
            log_tour += [pop.tourlist[min_index].tour]
            if i % 5000 == 0:
                log_len += [min_index]

    return log_tour, log_len


"""
order crossover + scramble_mutation + elitism_selection

"""


def EA2(population_size, tsp_path, opt_path, batch_size):
    mutation_possibility = 6
    tsp = TSPProblem(tsp_path, opt_path)
    pop = Population(tsp, population_size)
    # initial
    pop.ini_tourlist()
    pop.set_length()
    pop.set_adaptability()
    log_tour = []
    log_len = []
    print("BS:",batch_size)
    for i in range(batch_size):
        # optimize 1/3 parents
        parents_list = Selection().elitism_selection(int(pop.len / 3), tsp, pop.len, pop)
        temp_list = pop.tourlist
        temp_list.sort(reverse = True)
        temp_list[0].calDis()
        print(temp_list[0].length)


        parents_pop = Population(tsp, pop.len)
        parents_pop.tourlist = parents_list
        child_list = []
        # cross random from parents
        if len(parents_list) % 2 == 0:
            child_list = parents_list
        else:
            child_list = parents_list[0:len(parents_list) - 1]
        while len(child_list) != population_size:
            pa1 = random.randint(0, int(pop.len / 3) - 1)
            pa2 = random.randint(0, int(pop.len / 3) - 1)
            # print(parents_pop.tourlist)

            pa1 = parents_pop.tourlist[pa1]  # individual
            pa2 = parents_pop.tourlist[pa2]

            # cross
            ch1, ch2 = crossOver(0, tsp).order_crossover(pa1, pa2)
            child_list.append(ch1)
            child_list.append(ch2)

        for j in range(4, population_size):
            rate = random.randint(1, 10)
            # mutation
            if rate <= mutation_possibility:
                child_list[j] = Mutation(0, tsp).scrambleMutation(child_list[j])
                child_list[j].calDis()
            # make the child population
            pop = Population(tsp, population_size)
            pop.tourlist = child_list
            pop.set_length()
            pop.set_adaptability()

            if i % 100 == 0:
                min_len = pop.tourlist[0].length
                min_index = 0
                for j in range(1, pop.len):
                    if pop.tourlist[j].length < min_len:
                        min_len = pop.tourlist[j].length
                        min_index = j
                log_tour += [pop.tourlist[min_index].tour]
                if i % 5000 == 0:
                    log_len += [min_index]
        temp_list = pop.tourlist
        temp_list.sort(reverse=True)
        temp_list[0].calDis()
    return log_tour, log_len, pop


"""
order crossover + inversion_mutation + elitism_selection

"""


def EA3(population_size, tsp_path, opt_path, batch_size):
    mutation_possibility = 6
    tsp = TSPProblem(tsp_path, opt_path)
    pop = Population(tsp, population_size)

    # initial
    pop.ini_tourlist()
    pop.set_length()
    pop.set_adaptability()

    log_tour = []
    log_len = []

    for i in range(batch_size):
        # optimize 1/3 parents
        parents_list = Selection().elitism_selection(int(pop.len / 3), tsp, pop.len, pop)
        parents_pop = Population(tsp, pop.len)
        parents_pop.tourlist = parents_list

        child_list = []

        # cross random from parents
        if len(parents_list) % 2 == 0:
            child_list = parents_list
        else:
            child_list = parents_list[0:len(parents_list) - 1]

        while len(child_list) != population_size:
            pa1 = random.randint(0, int(pop.len / 3) - 1)
            pa2 = random.randint(0, int(pop.len / 3) - 1)

            pa1 = parents_pop.tourlist[pa1]
            pa2 = parents_pop.tourlist[pa2]

            # cross
            ch1, ch2 = crossOver(0, tsp).order_crossover(pa1, pa2)
            child_list.append(ch1)
            child_list.append(ch2)

        for j in range(population_size):
            rate = random.randint(1, 10)
            # mutation
            if rate <= mutation_possibility:
                child_list[j] = Mutation(0, tsp).invertionMutation(child_list[j])

            # make the child population
            pop = Population(tsp, population_size)
            pop.tourlist = child_list
            pop.set_length()
            pop.set_adaptability()

            if i % 100 == 0:
                min_len = pop.tourlist[0].length
                min_index = 0
                for j in range(1, pop.len):
                    if pop.tourlist[j].length < min_len:
                        min_len = pop.tourlist[j].length
                        min_index = j
                log_tour += [pop.tourlist[min_index].tour]
                if i % 5000 == 0:
                    log_len += [min_index]

    return log_tour, log_len
