from Algorithms import EA1,EA2,EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader
import numpy as np

n = 1 #减少随机误差
population_size = 10
tsp_path = "dataSet/tsp/eil51.tsp"
opt_path = "dataSet/opt_tour/eil51.opt.tour"
batch_size = 10000

def printOpt(pop):
    temp_list = pop.tourlist
    temp_list.sort(reverse = True)
    print("最短路径：",end='')
    temp_list[0].calDis()
    print(temp_list[0].length)


# def printGroup(G0):
#     A = 0
#     B = []
#     for t in G0:
#         A = A +printOptLength(t)
#         B.append(printOptLength(t))
#     print(min(B))
#     return  A

# def printOptLength(tour):
#     location1 = "dataSet/tsp/eil51.tsp"
#     location2 = "dataSet/opt_tour/eil51.opt.tour"
#     TSP0 = TSPProblem(location1, location2)
#     Ind =Individual(TSP0)
#     Ind.tour = tour
#     Ind.calDis()
#     return Ind.length



with open("eil51_ave.txt", 'w') as f:
    with open("eil51_log_ave.txt", 'w') as f2:
        f.write("filepath:%s\n"%tsp_path)
        f2.write("filepath:%s\n"%tsp_path)
        lens = []
        A = 0
        for t in range(n):
            A = 0
            print(t)
            f.write("\n%d\n"%t)
            f2.write("\n%d\n"%t)

            f.write("ans:\n")
            tsp = TSPProblem(tsp_path, opt_path)

            #test ea3
            f.write("average ea3:\n")
            f2.write("average ea3:\n")
            log_tour, log_len, pop = EA2(population_size, tsp_path, opt_path, batch_size)

            printOpt(pop)
            #print(printGroup(log_tour))

            for tour in log_tour:
                tour_new = [str(x) for x in tour]
                # ss = "\n"
                # f2.write(ss)
                # A = A + printOptLength(tour)
                s = ' '.join(tour_new)
                f2.write(s)
                f2.write("\n")

            f.write("batch_size:%d\n"%(10000))
            #f.write(str(log_len[1]))
            f.write("\n")
            f.write("***********************************************")
            f2.write("***********************************************")
            lens += [log_len[1]]
            print("Cost A",A)

        mean = np.mean(lens)
        std = np.std(lens, ddof = 1)
        f.write("average cost:%f\n"%(mean))
        f.write("standard deviation:%f\n"%(std))


