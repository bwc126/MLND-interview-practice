# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
#
# Vertices are represented as unique strings. The function definition should be question3(G)

def question3(G):
    # G is going to be a dictionary where keys are letters, values are lists of tuples. Each tuple has a letter for a node which connects to its key and an integer specifying its edge weight with that node.
    return
    # We could build an adj. matrix, make sure the values on either side of the diagonal are ones, like below (for 'graph_one' example), then convert it back to an adjacency list.
    # [(0 1 0 0),
    #  (1 0 1 0),
    #  (0 1 0 1),
    #  (0 0 1 0)]


    # Goal: return an adjacency dictionary of lists of tuples. Something like:
    # {'A': [('B', 1)],
    #  'B': [('A', 1), ('C', 1)],
    #  'C': [('B', 1)]}
    # Generally, the result will have n edges where n is the number of nodes. This means there will be 2n-2 total tuples in the finished adjacency list.


# Test Cases
graph_one = {'A': [('B', 3), ('C', 6), ('D', 4)],
             'B': [('A', 3), ('C',2), ('D',9)],
             'C': [('A', 6), ('B', 2)],
             'D': [('A', 4), ('B', 9)]}
question3(graph_one)
# Should return something like
    # {'A': [('B',1)],
    #  'B': [('A',1), ('C', 1)],
    #  'C': [('B', 1), ('D', 1)],
    #  'D': [('C', 1)]}
