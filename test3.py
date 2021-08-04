from Algorithms import EA1, EA2, EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader
import numpy as np

filelist = ["data/eil51.tsp", "data/eil76.tsp", "data/eil101.tsp", "data/kroA100.tsp", "data/kroC100.tsp",
            "data/kroD100.tsp", "data/lin105.tsp", "data/pcb442.tsp", "data/pr2392.tsp", "data/st70.tsp"]
with open("opt_tour_ans.txt", 'w') as f:
    for filename in filelist:
        tsp = TSPProblem(filename)
        # tsp.get_opt_tour()
        f.write("problem:%s\n" % tsp.NAME)
        ind = Individual(tsp)
        ind.tour = tsp.OptSelction
        ind.calDis()
        f.write("length:%f\n" % (ind.length))
        f.write("*********************************************************************\n")
