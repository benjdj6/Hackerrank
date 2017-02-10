import numpy
n = int(raw_input().split()[0])
a = []
b = []
for i in range(n):
    a.append(map(int, raw_input().split()))

for i in range(n):
    b.append(map(int, raw_input().split()))

print numpy.dot(a, b)
