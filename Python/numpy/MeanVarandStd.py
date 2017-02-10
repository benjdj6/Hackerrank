import numpy

n, m = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(map(int, raw_input().split()))

print numpy.mean(a, axis=1)
print numpy.var(a, axis=0)
print numpy.std(a)
