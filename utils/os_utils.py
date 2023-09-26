import os 

def path_coordinates(file_name:str) ->str:
    """
    Input : a string, file name
    Output : the path the the file in coordinates folder
    """
    return os.path.join("coordinates", file_name)