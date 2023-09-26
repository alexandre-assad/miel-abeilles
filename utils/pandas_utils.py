import pandas as pd
from utils.os_utils import path_coordinates


def coordinates_scrap() ->list[list[int]]:
    """
    Input : no input
    Output : a list of list of two ints, a list of coordinates x and y for each flowers
    """
    flowers = []
    df = pd.read_csv(path_coordinates("flowers_coordinates.csv"))
    for i in range(len(df)):
        flowers.append([df["x"][i],df["y"][i]])
    return flowers