from Algorithms import EA1, EA2, EA3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import dataLoader

population_size = 10
# tsp_path = "dataSet/tsp/eil51.tsp"
# opt_path = "dataSet/opt_tour/eil51.opt.tour"
batch_size = 20000

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
txt_list = ["Experiment1_logfiles/eil51.txt", "Experiment1_logfiles/eil76.txt", "Experiment1_logfiles/eil101.txt",
            "Experiment1_logfiles/kroA100.txt",
            "Experiment1_logfiles/kroC100.txt",
            "Experiment1_logfiles/kroD100.txt", "Experiment1_logfiles/lin105.txt", "Experiment1_logfiles/pcb442.txt",
            "Experiment1_logfiles/pr2392.txt",
            "Experiment1_logfiles/st70.txt"]
log_list = ["Experiment1_logfiles/eil51_log.txt", "Experiment1_logfiles/eil76_log.txt",
            "Experiment1_logfiles/eil101_log.txt", "Experiment1_logfiles/kroA100_log.txt",
            "Experiment1_logfiles/kroC100_log.txt",
            "Experiment1_logfiles/kroD100_log.txt", "Experiment1_logfiles/lin105_log.txt",
            "Experiment1_logfiles/pcb442_log.txt", "Experiment1_logfiles/pr2392_log.txt",
            "Experiment1_logfiles/st70_log.txt"]

for i in (0, 1):
    tsp_path = filelist[i]
    opt_path = optlist[i]
    txt_file = txt_list[i]
    log_file = log_list[i]
    with open(txt_file, 'w') as f:
        with open(log_file, 'w') as f2:
            f.write("filepath:%s\n" % tsp_path)
            f2.write("filepath:%s\n" % tsp_path)

            for population_size in (10, 20, 50, 100):
                print("population_size:%d\n" % population_size)
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
                f.write("test EA1:\n")
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
                    f.write("\n\n")
                    i += 1

                # test ea2

                print("TestEA2")
                f.write("test EA2:\n")
                f2.write("test EA2:\n")
                log_tour, log_len, pop = EA2(population_size, tsp_path, opt_path, batch_size)
                for tour in log_tour:
                    tour = [str(x) for x in tour]
                    s = ' '.join(tour)
                    f2.write(s)
                    f2.write("\n")
                i = 1
                for len in log_len:
                    f.write("batch_size:%d\n" % (i * 5000))
                    f.write(str(len))
                    f.write("\n\n")
                    i += 1

                # test ea3

                print("TestEA3")
                f.write("test EA3:\n")
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
                    f.write(str(len))
                    f.write("\n\n")
                    i += 1
                print(1)
                f.write("***********************************************")
                f2.write("***********************************************")
