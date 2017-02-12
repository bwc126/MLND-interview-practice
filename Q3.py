# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
#
# Vertices are represented as unique strings. The function definition should be question3(G)

def question3(G):
    # G is going to be a dictionary where keys are letters, values are lists of tuples. Each tuple has a letter for a node which connects to its key and an integer specifying its edge weight with that node.
    # We could build an adj. matrix, make sure the values on either side of the diagonal are ones, like below (for 'graph_one' example), then convert it back to an adjacency list.
    # [(0 2 0),
    #  (2 0 5),
    #  (0 5 0)]
    # Since our number of operations scales approximately with the number of units in the diagonal, our complexity grows approximately linearly with n, so ~O(n). We'd also need to handle instances where the actual edge weights are lowest when the graph has some nodes with more than 2 connections. Also, we need to preserve the original edge weights, and find the lowest ones to use in our minimum spanning tree, requiring ~O(W). **This might involve finding the lowest weights for each key, preserving only those, and then backfilling to make the graph list correct. **

    # For each key, find the lowest weight tuple. We'd keep the B tuple in A, the A tuple in B, the B tuple in C.
    for key in G:
        min = float('inf')
        keeper = ()
        for node, weight in G[key]:
            # print node, weight
            if weight < min:
                min = weight
                keeper = (node, weight)
        G[key] = [keeper]
        print key, G[key]

    # Back-fill any keys which don't have tuples corresponding to tuples that other keys have. We'd have to back-fill the C tuple within B to correspond to C's B tuple. Adjacency matrix might make this easier, as it would be a matter of reversing the coordinates for a position and making sure there's a corresponding value a that position. E.g., if there's a '3' at 1,2, there should be the same value at 2,1. This matrix can then be converted back to a list. Using only lists,  during the backfill step, for each key, we'd need to look up any other key in its tuple and see if it has a reference back to the parent key. For the present solution, a purely graph lists approach was used. 

    # For each key, (hereafter the 'primary key') for each tuple (should be just one per primary key at this point), check the key named in that tuple, if that key lacks a reference to our primary key, we add it back using our primary key's tuple for the edge weight.

    for key in G:
        node, weight = G[key][0]
        tup = (key,weight)
        if tup not in G[node]:
            G[node].append(tup)


    # Goal: return an adjacency dictionary of lists of tuples. Something like:
    # {'A': [('B', 1)],
    #  'B': [('A', 1), ('C', 1)],
    #  'C': [('B', 1)]}
    # Generally, the result will have n edges where n is the number of nodes. This means there will be something like 2n-2 total tuples in the finished adjacency list. Since we have one first degree and one two-degree 'for' loops, our complexity is ~O(n*W) with n = number of nodes, W = number of weights
    return G


# Test Cases
graph_one = {'A': [('B', 3), ('C', 6), ('D', 4)],
             'B': [('A', 3), ('C',2), ('D',9)],
             'C': [('A', 6), ('B', 2)],
             'D': [('A', 4), ('B', 9)]}
print question3(graph_one)
# Should return something like
    # {'A': [('B',3), ('D', 4)],
    #  'B': [('A',3), ('C', 2)],
    #  'C': [('B', 2)],
    #  'D': [('A', 4)]}
