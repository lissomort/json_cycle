import json


def read_json(path_to_json: str) -> dict:
    """
    Read json file from the given path and return 
    python dict
    """
    # open JSON file
    f = open(path_to_json)  

    # return pythonic dictionary object
    data = json.load(f)

    # close the file
    f.close()
    return data


def is_correct_cycle(stack: list, all_cycles: list) -> bool:
    sorted_cycles = [set(sorted(c)) for c in all_cycles]
    if len(stack) > 2 and stack[0] == stack[-1] and set(sorted(stack)) not in sorted_cycles:
        return True
    return False
