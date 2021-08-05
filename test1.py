from Algorithms import EA1, EA2, EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader

population_size = 10
tsp_path = "dataSet/tsp/eil51.tsp"
opt_path = "dataSet/opt_tour/eil51.opt.tour"
batch_size = 10000

with open("eil51.txt", 'w') as f:
    with open('ei51_log.txt', 'w') as f2:
        f.write("filepath:%s\n" % tsp_path)
        f2.write("filepath:%s\n" % tsp_path)

        for population_size in (10, 20):
            f.write("\n")
            f2.write("\n")
            f.write("population_size:%d\n" % population_size)
            f2.write("population_size:%d\n" % population_size)

            f.write("ans:\n")
            tsp = TSPProblem(tsp_path, opt_path)

            ans = Individual(TSPProblem(tsp_path, opt_path))
            Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION = dataLoader(opt_path, 0).Loading()
            ans.tour = TOUR_SECTION
            ans.calDis()
            f.write(str(ans.length))
            f.write("\n")
            # test EA1
            print("TestEA1")
            f.write("test EA1:")
            f2.write("test EA1:\n")
            log_tour, log_len = EA1(population_size, tsp_path, opt_path, batch_size)

            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")


            i = 1
            for len in log_len:
                f.write("batch_size:%d\n" % (i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1
            
            # test ea2

            print("TestEA2")
            f.write("test ea2:")
            f2.write("test ea2:\n")
            log_tour, log_len,pop = EA2(population_size, tsp_path, opt_path, batch_size)
            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")
            i = 1
            for len in log_len:
                f.write("batch_size:%d\n" % (i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1

            # test ea3

            print("TestEA3")
            f.write("test ea3:")
            f2.write("test ea3:\n")
            log_tour, log_len = EA3(population_size, tsp_path, opt_path, batch_size)
            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")
            i = 1
            for len in log_len:
                f.write("batch_size:%d\n" % (i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1
            print(1)
            f.write("***********************************************")
            f2.write("***********************************************")




