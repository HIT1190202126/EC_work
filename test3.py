from Algorithms import EA1, EA2, EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader
import numpy as np

filelist = ["dataSet/tsp/eil51.tsp", "dataSet/tsp/eil76.tsp", "dataSet/tsp/eil101.tsp", "dataSet/tsp/kroA100.tsp",
            "dataSet/tsp/kroC100.tsp",
            "dataSet/tsp/kroD100.tsp", "dataSet/tsp/lin105.tsp", "dataSet/tsp/pcb442.tsp", "dataSet/tsp/pr2392.tsp", "dataSet/tsp/st70.tsp"]
optlist = ["dataSet/opt_tour/eil51.opt.tour", "dataSet/opt_tour/eil76.opt.tour", "dataSet/opt_tour/eil101.opt.tour", "dataSet/opt_tour/kroA100.opt.tour",
           "dataSet/opt_tour/kroC100.opt.tour",
           "dataSet/opt_tour/kroD100.opt.tour", "dataSet/opt_tour/lin105.opt.tour", "dataSet/opt_tour/pcb442.opt.tour", "dataSet/opt_tour/pr2392.opt.tour",
           "dataSet/opt_tour/st70.opt.tour"]

with open("opt_tour_ans.txt", 'w') as f:
    for i in range(10):
        tsp = TSPProblem(filelist[i], optlist[i])
        tsp.get_opt_tour(optlist[i])
        f.write("problem:%s\n" % tsp.Name)
        ind = Individual(tsp)
        ind.tour = tsp.OptSelction
        ind.calDis()
        f.write("length:%f\n" % (ind.length))
        f.write("*********************************************************************\n")
