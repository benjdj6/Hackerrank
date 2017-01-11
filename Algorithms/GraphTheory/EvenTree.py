# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node(object):

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children


vertices = []
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]


def countSubTree(root):
    count = 0
    if root.getChildren():
        for c in root.getChildren():
            count += countSubTree(c)
    return count + 1


for i in range(1, n + 1):
    vertices.append(Node(i))

for j in range(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]

    vertices[v - 1].addChild(vertices[u - 1])

edges = -1
for v in vertices:
    if countSubTree(v) % 2 == 0:
        edges += 1
print edges
