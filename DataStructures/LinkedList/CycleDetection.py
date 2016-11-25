"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head.next and head.next.next:
        temp1 = head.next
        temp2 = head.next.next
        while temp1 and temp2:
            if temp1 == temp2:
                return True
            if not temp2.next or not temp2.next.next:
                return False
            temp1 = temp1.next
            temp2 = temp2.next.next
    return False