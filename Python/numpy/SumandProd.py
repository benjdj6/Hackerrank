import numpy

n, m = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(map(int, raw_input().split()))

a = numpy.array(a)
a = numpy.sum(a, axis=0)

print numpy.prod(a)
