

def question1(s='',t=''):

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
print question1() # Should be None


import math

def question2(a=''):

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

    result = ''
    width = len(a)
    old_result = ''
    new_result = ''
    while width >= 2:
        offsets = len(a) - width + 1
        for offset in range(offsets):
            new_result = test(a, offset, width)
        if (len(new_result) < len(old_result)):
            return old_result
        if (len(new_result) > len(old_result)):
            old_result = new_result
        width -= 1
    return old_result

print question2('abab') # Should be 'bab'
print question2('avva') # Should be 'avva'
print question2('avcva') # Should be 'avcva'
print question2('racecar') # Should be 'racecar'
print question2('ihaveafastracecar') # Should be 'racecar'
print question2('alsjsdfjhsdlkfhliearbfienflinlifiuhgleiuhhhgh') # Edge Case: Should be 'hgh'
print question2('') # Edge Case: Should be ''
print question2() # Edge Case: Should be ''

def question3(G={}):

    for key in G:
        min = float('inf')
        keeper = ()
        for node, weight in G[key]:

            if weight < min:
                min = weight
                keeper = (node, weight)
        G[key] = [keeper]

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
graph_two = {}
print question3(graph_two) # Edge Case: Should return {}
print question3() # Edge Case: Should return {}

import copy
def question4(T, r, n1, n2):
    if not T:
        return

    nodes = {}

    M = copy.deepcopy(T)
    for row in range(len(M)):
        if 1 in M[row]:
            children = []
            for child in range(M[row].count(1)):
                loc = M[row].index(1)
                children.append(loc)
                M[row][loc] = 0
            nodes[row] = children


    def find_ancestors(val, ancestors, tree):

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

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def question5(ll, m):
    output = 0
    def search_list(start, val):
        if val == 0:
            output = start.value
            return start.value
        elif start:
            if start.right:
                return search_list(start.right, val-1)
            elif start.left:
            
                return search_list(start.left, val-1)

    return search_list(ll, m)

# Test Cases
l_l = Node(1)
l_l.right = Node(2)
l_l.right.right = Node(3)
l_l.right.right.right = Node(5)
l_l.right.right.right.right = Node(4)

print question5(l_l,4) # Should be 4
print question5(l_l,2) # Should be 3
print question5(l_l,0) # Should be 1
print question5(l_l, -1) # Edge case: should be None

c_c = Node(5)
c_c.left = Node(3)
c_c.left.left = Node(6)
c_c.left.left.left = Node(12)
c_c.left.left.left.left = Node(13)

print question5(c_c,2) # Should be 6
print question5(c_c,3) # Should be 12
print question5(c_c,5) # Edge case: Should be None
