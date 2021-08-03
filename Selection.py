import random

class Selection:
    def fitness_proportional_selection(self, n, tsp ,len):
        """
        fitness poportionate selection,
        calculate the fitness of each individual,
        generate several random numbers,
        and select the corresponding individual according to the random number and fitness

        :param n: the number of selected individuals
        :param tsp: tsp problem
        :param len: the number of all individuals
        :return: the selected individuals
        """

        popu = Population(tsp, len)
        sum = 0 #the sum of adaptabiliity
        probabilitydict = {}
        for individual in popu.tourlist:
            sum += individual.adaptability
        for individual in popu.tourlist:
            probabilitydict[individual] = individual.adaptability/sum
        accu_probility_dic = {} # the probability of accumulation
        accu = 0
        for individual in popu.tourlist:
            accu += probabilitydict[individual]
            accu_probility_dic[individual] = accu

        selected_list = []

        while len(selected_list) < n:
            random_probability = random.random()
            # if the fitness of the first individual is bigger than the random_probability, select the first one
            if accu_probility_dic[popu.tourlist[0]]>random_probability and popu.tourlist[0] not in selected_list:
                selected_list.append(popu.tourlist[0])
            # else, find the individual whose accurated probability is bigger than the random probability, and select it
            else:
                for item in accu_probility_dic:
                    if accu_probility_dic[item] > random_probability and item not in selected_list:
                        selected_list.append(item)

        # create the new population accroding to the selected individuals
        child_population = Population(len(selected_list), tsp)
        child_population.tourlist = selected_list
        return child_population

    def tournament_selection(self, n, k, tsp, len):
        """
        k individuals are selected each time,
        and the best one of the k individuals is selected according to the fitness.
        A total of N times

        :param k: the number of selected individuals of each time
        :param n: the number of selected individuals
        :param tsp: tsp problem
        :param len: the number of all individuals
        :return: the selected individuals
        """
        popu = Population(tsp, len)
        selected_list = []
        while len(selected_list) < n:
            k_individule_list = []
            while len(k_individule_list) < k:
                random_id = random.randint(0, len-1)
                # select the individual corresponding random id
                if popu.tourlist[random_id] not in k_individule_list:
                    k_individule_list.append(popu.tourlist[random_id])
            # sort them by their fitness
            k_individule_list.sort(reverse = True)
            # select the biggest one, and it cannot be selected before
            for i in range(k):
                if k_individule_list[i] not in selected_list:
                    selected_list.append(k_individule_list[i])
        child_population = Population(len(selected_list), tsp)
        child_population.tourlist = selected_list
        return child_population

    def elitism_selection(self, n ,tsp, len):
        """
        According to the fitness ranking,
        select the first n individuals with the highest fitness.

        :param n: the number of selected individuals
        :param tsp: tsp problem
        :param len: the number of all individuals
        :return: the selected individuals
        """
        poup = Population(tsp, len)
        temp_list = popu.tourlist
        # sort all of them by their fitness
        temp_list.sort()
        # select the top n individuals
        selected_list = temp_list[:n]
        child_population = Population(len(selected_list), tsp)
        child_population.tourlist = selected_list
        return child_population
