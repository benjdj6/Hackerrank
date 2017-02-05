"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    dup = {}
    curr = head
    dup[curr.data] = 1
    while curr and curr.next:
        if curr.next.data not in dup:
            dup[curr.next.data] = 1
            curr = curr.next
        else:
            curr.next = curr.next.next
    return head
