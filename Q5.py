# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
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
