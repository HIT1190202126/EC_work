from Algorithms import EA1,EA2,EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader
import numpy as np

n = 10 
population_size = 50
tsp_path = "data/eil51.tsp"
opt_path = "data/eil51.opt.tour"
batch_size = 1000

with open("eil51_ave.txt", 'w') as f:
    with open("eil51_log_ave.txt", 'w') as f2:
        f.write("filepath:%s\n"%tsp_path)
        f2.write("filepath:%s\n"%tsp_path)
        lens = []
        for t in range(n):
            f.write("\n%d\n"%t)
            f2.write("\n%d\n"%t)

            f.write("ans:\n")
            tsp = TSPProblem(tsp_path, opt_path)

            #test ea3
            f.write("average ea3:\n")
            f2.write("average ea3:\n")
            log_tour, log_len = EA3(population_size, tsp_path, opt_path, batch_size)
            
            for tour in log_tour:
                tour_new = [str(x) for x in tour]
                s = ' '.join(tour_new)
                f2.write(s)
                f2.write("\n")
            
            f.write("batch_size:%d\n"%(10000))
            f.write(str(log_len[1]))
            f.write("\n")
            f.write("***********************************************")
            f2.write("***********************************************")
            lens += [log_len[1]]
        
        mean = np.mean(lens)
        std = np.std(lens, ddof = 1)
        f.write("average cost:%f\n"%(mean))
        f.write("standard deviation:%f\n"%(std))


