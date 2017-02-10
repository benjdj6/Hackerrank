import numpy
n = int(raw_input())
a = []
for i in range(n):
    a.append(map(float, raw_input().split()))

print numpy.linalg.det(a)
