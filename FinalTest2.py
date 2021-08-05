from Algorithms import EA1, EA2, EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader
import numpy as np

population_size = 50
# tsp_path = "dataSet/tsp/eil51.tsp"
# opt_path = "dataSet/opt_tour/eil51.opt.tour"
batch_size = 10000

filelist = ["dataSet/tsp/eil51.tsp", "dataSet/tsp/eil76.tsp", "dataSet/tsp/eil101.tsp", "dataSet/tsp/kroA100.tsp",
            "dataSet/tsp/kroC100.tsp",
            "dataSet/tsp/kroD100.tsp", "dataSet/tsp/lin105.tsp", "dataSet/tsp/pcb442.tsp", "dataSet/tsp/pr2392.tsp",
            "dataSet/tsp/st70.tsp"]
optlist = ["dataSet/opt_tour/eil51.opt.tour", "dataSet/opt_tour/eil76.opt.tour", "dataSet/opt_tour/eil101.opt.tour",
           "dataSet/opt_tour/kroA100.opt.tour",
           "dataSet/opt_tour/kroC100.opt.tour",
           "dataSet/opt_tour/kroD100.opt.tour", "dataSet/opt_tour/lin105.opt.tour", "dataSet/opt_tour/pcb442.opt.tour",
           "dataSet/opt_tour/pr2392.opt.tour",
           "dataSet/opt_tour/st70.opt.tour"]
txt_list = ["Experiment2_logfiles/eil51.txt", "Experiment2_logfiles/eil76.txt", "Experiment2_logfiles/eil101.txt",
            "Experiment2_logfiles/kroA100.txt",
            "Experiment2_logfiles/kroC100.txt",
            "Experiment2_logfiles/kroD100.txt", "Experiment2_logfiles/lin105.txt", "Experiment2_logfiles/pcb442.txt",
            "Experiment2_logfiles/pr2392.txt",
            "Experiment2_logfiles/st70.txt"]
log_list = ["Experiment2_logfiles/eil51_log.txt", "Experiment2_logfiles/eil76_log.txt",
            "Experiment2_logfiles/eil101_log.txt", "Experiment2_logfiles/kroA100_log.txt",
            "Experiment2_logfiles/kroC100_log.txt",
            "Experiment2_logfiles/kroD100_log.txt", "Experiment2_logfiles/lin105_log.txt",
            "Experiment2_logfiles/pcb442_log.txt", "Experiment2_logfiles/pr2392_log.txt",
            "Experiment2_logfiles/st70_log.txt"]

for i in range(1):
    # select ith item
    tsp_path = filelist[9]
    opt_path = optlist[9]
    txt_file = txt_list[9]
    log_file = log_list[9]

    with open(txt_file, 'w') as f:
        with open(log_file, 'w') as f2:
            print(tsp_path)
            f.write("filepath:%s\n" % tsp_path)
            f2.write("filepath:%s\n" % tsp_path)

            f.write("\n")
            f2.write("\n")
            f.write("population_size:%d\n" % population_size)
            f2.write("population_size:%d\n" % population_size)

            f.write("ans:\n")
            costList = []
            for round in range(3):
                tsp = TSPProblem(tsp_path, opt_path)

                ans = Individual(TSPProblem(tsp_path, opt_path))
                Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION = dataLoader(opt_path, 0).Loading()
                ans.tour = TOUR_SECTION
                ans.calDis()
                print("Best:", ans.length)
                f.write(str(ans.length))
                f.write("\n")
                # test EA2
                print("TestEA3")
                f.write("test EA3:")
                f2.write("test EA3:\n")
                log_tour, log_len, pop = EA3(population_size, tsp_path, opt_path, batch_size)

                for tour in log_tour:
                    tour = [str(x) for x in tour]
                    s = ' '.join(tour)
                    f2.write(s)
                    f2.write("\n")

                i = 1

                for len in log_len:
                    f.write("batch_size:%d\n" % (i * 5000))
                    print(len)
                    f.write(str(len))
                    f.write("\n")
                    i += 1

                costList.append(min(log_len))

                f.write("***********************************************")
                f2.write("***********************************************")
            str0 = "\naverage cost:" + str(np.mean(costList)) + "\n standard deviation:" + str(np.std(costList))
            print(str0)
            f.write(str0)
