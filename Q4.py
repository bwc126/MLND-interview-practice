# Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
#
# and the answer would be 3.

# The matrix contains a number of rows equal to one plus the highest number in the BST. The index of a list within the matrix corresponds to each node's value. If the list for a node contains a 1, that node has a child whose value is the index of the position of the 1 within the list. For the example given above, the BST would have a 3 at the root, 0 on the left, 4 on the right. The 0 would have a child of 1 on the right.

# The signature question4(T, r, n1, n2) includes T, a binary matrix as described previously, r, a non-neg integer corresponding to the value of the root. n1, n2 are each non-neg ints representing the two nodes for which we need to find the greatest common ancestor node. We can assume n1, n2 might be in any order, that both nodes are in fact within the tree, and the BST conforms to standard rules for a BST.
import copy
def question4(T, r, n1, n2):
    if not T:
        return
    # Since r is the value of the root, we should look within T and find the list at that index value to see what children our root has. Ultimately, we need to find n1, n2's parents, and see if they're actually the same node, and if not, how far up the tree we need to look to find the greatest common ancestor for them. If the root is the immediate parent of n1,n2, then we've found our result. Otherwise, we need to keep moving up the tree until we find a parent node both n1,n2 have in common.

    # Start by discarding trivial rows, storing the remaining rows with their node value in a dictionary as a key, and a list of their children as values. 0: [1] would be one such dictionary entry for the example in the question definition.
    nodes = {}
    # print T
    M = copy.deepcopy(T)
    for row in range(len(M)):
        if 1 in M[row]:
            children = []
            for child in range(M[row].count(1)):
                loc = M[row].index(1)
                children.append(loc)
                M[row][loc] = 0
            nodes[row] = children

    # print nodes
    # print T == M
    # We then recursively find all parents for each of n1, n2 all the way to the root.
    def find_ancestors(val, ancestors, tree):
        # print val, ancestors, tree
        if val == r:
            return ancestors
        else:
            for node in tree:
                if val in tree[node]:
                    ancestors.append(node)
                    return find_ancestors(node, ancestors, tree)


    a_1 = []
    a_2 = []
    a_1 = find_ancestors(n1, a_1, nodes)
    a_2 = find_ancestors(n2, a_2, nodes)
    # print a_1, a_2

    # Compare the lists of ancestors. We should return the first one that appears in both. We 'for' loop through one, check if it's in the other, and if it is, we return that value immediately, ending the function qeustion4().
    if not a_1 or not a_2:
        return
    for ancestor in a_1:
        if ancestor in a_2:
            return ancestor




# Test Cases
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 0
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,1,0,0,0,0,0,0,0,0], # 3
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,1,0,0,0,0,0,0,0], # 6
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 9
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 12
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]
root = 8
n_1, n_2 = 4, 7
print question4(matrix, root, n_1, n_2) # Should be 6

n_3, n_4 = 1, 6
print question4(matrix, root, n_3, n_4) # Should be 3

n_5, n_6 = 4, 10
print question4(matrix, root, n_5, n_6) # Should be 8

n_7, n_8 = 16, 0
print question4(matrix, root, n_7, n_8) # Edge case: should be None

n_9, n_10 = 4, 10
print question4(None, root, n_9, n_10) # Edge case: should be None
