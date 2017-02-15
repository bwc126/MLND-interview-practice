# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
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
                # We NEED return statements here and above because if this call returns any ouput, we'll need to return it to the execution context above the one this comment is in
                return search_list(start.left, val-1)

    return search_list(ll, m)

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
