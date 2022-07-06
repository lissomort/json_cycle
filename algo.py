"""
Algorithm module for all search functions
Searching cycles in given dictionary like data
via algorithm based on DFS graph algorithm
"""

from data import is_correct_cycle


def util_rec_function(full_data: dict, v: str, visited: list, stack: list) -> bool:
    """
    Helper function for recursive traverse through dict
    """

    # mark current as visited and put into stack
    # for chaining cycle

    visited.append(v)
    stack.append(v)

    # call recursively for all connected names
    # if the name is already visited and stored in stack
    # we have a cycle
    for name in full_data[v]:
        # check if the name is not in a keys at all
        if name not in full_data.keys():
            continue
        # if it is not visited - call to recursive function with this name
        if name not in visited:
            if util_rec_function(full_data, name, visited, stack):
                return True
        elif name in stack and name == stack[0]:
            stack.append(name)
            return True

        if name in stack:
            stack.remove(name)  # remove from stack before failing if we didn't remove it yet
        return False


def find_cycles(full_data: dict) -> list:
    """
        Find and return the list of cycles in json document
    """
    cycles = list()

    for name in full_data.keys():
        visited = list()
        stack = list()
        if name not in visited:
            if util_rec_function(full_data, name, visited, stack):
                # check for backedges, repeated cycles
                if is_correct_cycle(stack, cycles):
                    cycles.append(stack)
    return cycles
