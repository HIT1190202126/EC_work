import re


class dataLoader:
    """
    Loading data , need to specify the type of the data(opt.tour / tsp)
    """

    def __init__(self, path, type):
        """
        The constructor func
        :param path:the location of the opening file
        :param type:the type of the file (1 - tsp , 0 -opt)
        """
        self.file_path = path
        self.dataType = type

    def readOpt(self, String0):
        """
        read data from opt.tour String
        :param String: opt.tour String
        :return: Name,  COMMENT, TYPE, DIMENSION ,TOUR_SECTION(in List)
        """
        Name = re.match(r"NAME : (.*)", String0)[1]
        COMMENT = re.search(r"COMMENT : (.*)", String0)[1]
        TYPE = re.search(r"TYPE : (.*)", String0)[1]
        DIMENSION = re.search(r"DIMENSION : (.*)", String0)[1]
        split = String0.split("\n")
        Tour = []
        for s0 in split:
            if (s0 and s0[0] <= '9' and s0[0] >= '0'):
                Tour.append(int(s0))
        return Name, COMMENT, TYPE, DIMENSION, Tour

    def readTsp(self, String0):
        """
        read data from opt.tour String
        :param String: opt.tour String
        :return: Name,  COMMENT ,TYPE DIMENSION, EDGE_WEIGHT_TYPE ,NODE_COORD_SECTION(in List[list[int]])
        """
        Name = re.match(r"NAME : (.*)", String0)[1]
        COMMENT = re.search(r"COMMENT : (.*)", String0)[1]
        TYPE = re.search(r"TYPE : (.*)", String0)[1]
        DIMENSION = re.search(r"DIMENSION : (.*)", String0)[1]
        EDGE_WEIGHT_TYPE = re.search(r"EDGE_WEIGHT_TYPE : (.*)", String0)[1]
        NODE_COORD_SECTION = []
        split = String0.split("\n")
        for s0 in split:
            if (s0 and s0[0] <= '9' and s0[0] >= '0'):
                one = s0.split(" ")
                One = []
                One.append(float(one[0]))
                One.append(float(one[1]))
                One.append(float(one[2]))
                if (One != []):
                    NODE_COORD_SECTION.append(One)
        return Name, COMMENT, TYPE, DIMENSION, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION

    def Loading(self):
        """
        Reading data
        :return:
        """
        string0 = ""
        with open(self.file_path, "r") as f:
            string0 = f.read()
            if (self.dataType == 0):
                # opt
                Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION = self.readOpt(string0)
                return Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION
            elif (self.dataType == 1):
                # Tsp
                Name, COMMENT, TYPE, DIMENSION, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION = self.readTsp(string0)
                return Name, COMMENT, TYPE, DIMENSION, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION


# Test:
if __name__ == "__main__":
    location = "dataSet/tsp/eil51.tsp"
    Name, COMMENT, TYPE, DIMENSION, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION = dataLoader(location, 1).Loading()
    print(Name)
    print(COMMENT)
    print(TYPE)
    print(DIMENSION)
    print(EDGE_WEIGHT_TYPE)
    print(NODE_COORD_SECTION)
    location = "dataSet/opt_tour/eil51.opt.tour"
    Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION = dataLoader(location, 0).Loading()
    print(Name)
    print(COMMENT)
    print(TYPE)
    print(DIMENSION)
    print(TOUR_SECTION)
