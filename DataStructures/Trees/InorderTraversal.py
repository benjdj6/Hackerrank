"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    #Write your code here
    curr = root
    if curr:
        inOrder(curr.left)
        print curr.data,
        inOrder(curr.right)