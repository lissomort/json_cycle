"""
Algorithm module for all search functions
Searching cycles in given dictionary like data
via algorithm based on DFS graph algorithm
"""

from data import stack2list


def util_rec_function(full_data, v, visited, stack):
    """
    Helper function for recursive traverse through dict
    Args:
        full_data (dict): Input dict.
        v (str): current start point
        visited (dict): dict of visited names
        stack (list): stack for checking cyclic way
    """

    # mark current as visited and put into stack
    # for chaining cycle
    visited[v] = True
    stack[v] = True

    # call recursively for all connected names
    # if the name is already visited and stored in stack
    # we have cycle
    for name in full_data[v]:
        if name not in full_data.keys():
            continue
        if not visited[name]:
            if util_rec_function(full_data, name, visited, stack):
                return True, stack
        elif stack[name]:
            return True, stack

        stack[v] = False # remove from stack before failing
        return False, stack


def find_cycles(full_data):
    """

    """
    cycles = list()

    for name in full_data.keys():
        visited = full_data.fromkeys(full_data, False)
        stack = visited.copy()
        if not visited[name]:
            if util_rec_function(full_data, name, visited, stack):
                cycles.append(stack2list(stack))
    return cycles
