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
