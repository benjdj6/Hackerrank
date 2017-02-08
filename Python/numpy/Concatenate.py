import numpy

n, m, p = map(int, raw_input().split())
narr = []
marr = []
for i in range(n):
    narr.append(map(int, raw_input().split()))
for i in range(m):
    marr.append(map(int, raw_input().split()))

narr = numpy.array(narr)
marr = numpy.array(marr)
print numpy.concatenate((narr, marr), axis=0)
