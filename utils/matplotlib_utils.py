import matplotlib 
import matplotlib.pyplot as plt
from utils.os_utils import path_graphs


def graph_by_time(data:list) ->None:
    """
    Input : a list, a data of list with this structure : data = [[iteration0,average0],[iteration1,average1],...]
    Output : Save a png file of the graph of the data
    """
    time = []
    average_distance = []
    for measurement in data:
        time.append(measurement[0])
        average_distance.append(measurement[1])

    plt.plot(time,average_distance)
    plt.xlabel('Iterations')
    plt.ylabel('Average distance')
    plt.savefig(path_graphs('average_distance_graph.png'))