

def question1(s='',t=''):
    # We can replace within s each character that's in t with some placeholder character (hyphen in this example), and then check to see if there's a string of placeholder characters within s that correspond to the length of t. Since we want all possible anagrams of t to be covered, any of the characters in t can be in any position within s, and as long as they're adjacent in s and there are at least as many in s as there are in t, we can confidently declare some anagram of t is within s.

    # For each letter in t, if count in t > count in s, return false. This will handle counterexample when t has repeats that s lacks, and s has repeats that t lacks, but both have at least one of same letter such that the remaining logic int this program would mistakenly return true for a string of special characters with t's length appearing in s.
    if not s or not t:
        return
    test = ''
    for char in t:
        if t.count(char) > s.count(char):
            return False
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
print question1('aaab','bbba') # Should be False

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
    # We'll need to keep track of the lesser and greater node values to take full advantage of BST properties later on.
    n_1 = min(n1,n2)
    n_2 = max(n1,n2)
    # Lacking a BST matrix is a non-starter.
    if not T:
        return
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

    print nodes
    # This is strictly for handling the cases where n1 or n2 aren't in the BST. We build a simple list of all nodes in the tree to make sure n1 and n2 are actually in it before doing any more unnecessary computation.
    all_nodes = []
    for children in nodes.values():
        for node in children:
            all_nodes.append(node)
    all_nodes.extend(nodes.keys())
    print all_nodes
    if n1 not in all_nodes or n2 not in all_nodes:
        return
    # We could look through the keys of 'nodes', which will be every node that is a parent of any node in the tree, and the first one we find that has a value between n1, n2 is our LCA. This assumes the keys are in order of their level on the tree, but they don't need to be in order relative to the other nodes on their level, because only nodes between n1 and n2 in value can be a parent of both.
    for parent in nodes.keys():
        if parent < n_2 and parent > n_1:
            return parent

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
    link = ll
    # We'll handle negative places by returning 'None', since the problem doesn't specify otherwise.
    if m < 0:
        return
    # We iteratively grasp the link of interest, whether we've begun with the left or rightmost link of the chain
    while m > 0:
        # If we've reached a non-existant link, we can just return 'None', since the problem doesn't say otherwise. If we wanted to, we could figure out the length of the chain early on and just return 'None' right away, but that would require almost as much computation as the current approach anyway. Or, we could have a way of 'looping' back around to end up back in the chain starting on the other side again--but then we'd have more of a loop than a chain.
        if link:
            link = link.left or link.right
        else:
            return
        m -= 1
    # It's possible to exit the while loop without a link, so we handle that similarly to the other linkless case.
    if not link:
        return
    return link.value

l_l = Node(1)
l_l.right = Node(2)
l_l.right.right = Node(3)
l_l.right.right.right = Node(5)
l_l.right.right.right.right = Node(4)
v = int()

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
print question5(c_c,1000000) # Edge case: Should be None
