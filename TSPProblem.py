import re
import Read_data
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D


class TSPProblem:
    """
    The class which represents the TSP problem.
    Enable the construction of TSP problems from the files of the symmetric traveling salesperson problem of the TSPlib
    """
    def __init__(self,pathTsp,pathOpt):
        """
        The Constructor of the TSPproblem
        :param pathTsp: the path which points to the .tsp file
        :param pathOpt: the path which points to the .Opt file
        """
        '''
        Name : file name
        Comment : The Comment  of the file
        Dimension : The num of cities
        EdgeWeightType : Type of the edge
        Edges : List of Edges [[num-order src dst],.....]   
        '''
        Name, COMMENT, TYPE, DIMENSION, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION = Read_data.dataLoader(pathTsp,1).Loading()
        self.Name = Name
        self.Comment = COMMENT
        self.Dimension = int(DIMENSION)
        self.EdgeWeightType = EDGE_WEIGHT_TYPE
        self.Cities = NODE_COORD_SECTION
        Name, COMMENT, TYPE, DIMENSION, TOUR_SECTION = Read_data.dataLoader(pathOpt, 0).Loading()
        if(int(DIMENSION)!= self.Dimension):
            print("Dim Error!!")
            exit()
        self.OptSelction = TOUR_SECTION
        print("Initialization Complete")
        self.print_info()

    def print_info(self):
        """
        print the Info of the Tsp-problem to the CMD window
        """
        print("-------- TSP problem Info --------")
        print("Name:\t",self.Name)
        print("Comment:\t",self.Comment)
        print("EdgesWeghtType:\t",self.EdgeWeightType)
        print("-------- Edges --------")
        for t in self.Cities:
            print("City: ",t[0],"\t<",t[1],"\t",t[2],">")

        print("-------- OptPath --------\n",self.OptSelction)

    def plot(self,route):
        """
        Connect the points from route,and draw it out
        :param route: the point seq ,List<int>
        :return:
        """
        fig,ax0 = plt.subplots()
        #label out the points
        for e0 in self.Cities:
            ax0.scatter(e0[1],e0[2],c='b',s=20,alpha = 0.5)
        #connet the cities
        StartingPoint = int(route[0])
        i = 0
        for k in route:
            if i == 0:
                i=1
                dst = self.Cities[k-1]
            else:
                src = dst
                dst = self.Cities[k-1]
                ax0.add_line(Line2D([src[1],dst[1]],[src[2],dst[2]],linewidth = 1 ,color = 'r'))
        plt.plot()
        plt.show()
    def getSelfWay(self):
        """
        get our Way by calling our methods
        :return: List of Cities
        """
        pass
    def plotOpt(self):
        self.plot(self.OptSelction)

if __name__ == "__main__":
    location1 = "dataSet/eil51.tsp/eil51.tsp"
    location2 = "dataSet/eil51.opt.tour/eil51.opt.tour"
    TSP0 = TSPProblem(location1,location2)
    TSP0.plotOpt()