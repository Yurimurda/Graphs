
def getParents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1] == node:
            parents.append(pair[0])
    return parents


def dft_recursive(ancestors, node, distance):
    parents = getParents(ancestors, node)

    aged_one = (node, distance)

    for parent in parents: 
        pair = dft_recursive(ancestors, parent, distance + 1)
        if pair[1] > aged_one[1]:
            aged_one = pair
    
    return aged_one


def earliest_ancestor(ancestors, starting_node, distance=0):
    aged_one = dft_recursive(ancestors, starting_node, distance)

    if aged_one[0] == starting_node:
        return -1

    return aged_one[0]