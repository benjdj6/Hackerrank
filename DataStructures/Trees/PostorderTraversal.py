"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here
    curr = root
    if curr:
        postOrder(curr.left)
        postOrder(curr.right)
        print curr.data,