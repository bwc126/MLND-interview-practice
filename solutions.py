# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s,t):
    # We can replace within s each character that's in t with some placeholder character (hyphen in this example), and then check to see if there's a string of placeholder characters within s that correspond to the length of t. Since we want all possible anagrams of t to be covered, any of the characters in t can be in any position within s, and as long as they're adjacent in s and there are at least as many in s as there are in t, we can confidently declare some anagram of t is within s.
    if not s or not t:
        return
    test = ''
    for char in t:
        s = s.replace(char, '-')
    for i in range(len(t)):
        test += '-'
    if test in s:
        return True
    return False


print question1('udacity','da') # Should be True
print question1('udacity','ad') # Should be True
print question1('udacity','ciud') # Should be False
print question1('udacity','uy') # Should be False
print question1('sarsaparilla','apas') # Should be True
print question1('','') # Should be None

# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

import math

def question2(a):
# Steps might be:

    # Split the string in half, check if the reverse of this half is in the rest of the string
    def test(s, offset, width):
        stop = int(math.ceil(width/2))
        # print stop
        b = s[0+offset:stop+offset]
        c = s[stop+offset:width+offset]
        # print b, c
        if b in c[::-1]:
            return b+c
        else:
            return ''
    # Do this recursively and iteratively with successively smaller substrings at different frames within the string until we've exahusted the possibilities for two letters
    result = ''
    width = len(a)
    old_result = ''
    new_result = ''
    while width >= 2:
        offsets = len(a) - width + 1
        for offset in range(offsets):
            new_result = test(a, offset, width)
            # print 'exiting at ', offset, len(new_result), len(old_result)
        if (len(new_result) < len(old_result)):
            # print 'returning ', old_result
            return old_result
        if (len(new_result) > len(old_result)):
            # print 'setting new result', new_result
            old_result = new_result
        width -= 1
    return old_result
print question2('abab')
print question2('avva')
print question2('avcva')
print question2('racecar')
print question2('ihaveafastracecar')

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

# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def question5(ll, m):
    # print ll, m
    output = 0
    def search_list(start, val):
        # print start.value, val
        if val == 0:
            # print 'should be returning', start.value
            output = start.value
            return start.value
        elif start:
            # print 'start defined'
            if start.right:
                return search_list(start.right, val-1)
            elif start.left:
                # We NEED return statements here and above because if this call returns any ouput, we'll need to return it to the execution context above the one this comment is in
                return search_list(start.left, val-1)

    return search_list(ll, m)

l_l = Node(1)
l_l.right = Node(2)
l_l.right.right = Node(3)
l_l.right.right.right = Node(5)
l_l.right.right.right.right = Node(4)

print question5(l_l,4) # Should be 4
print question5(l_l,2) # Should be 3
print question5(l_l,0) # Should be 1

c_c = Node(5)
c_c.left = Node(3)
c_c.left.left = Node(6)
c_c.left.left.left = Node(12)
c_c.left.left.left.left = Node(13)

print question5(c_c,2) # Should be 6
print question5(c_c,3) # Should be 12
print question5(c_c,5) # Should be None
