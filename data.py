import json


def read_json(path_to_json):
    """
    Read json file from the given path and return 
    python dict
    Args:
        path_to_json (str): path to json file with data 

    Returns:
        dict: return a data in dictionary 
    """
    # open JSON file
    f = open(path_to_json)  

    # return pythonic dictionary object
    data = json.load(f)

    # close the file
    f.close()
    return data
