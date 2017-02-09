import numpy


n = map(int, raw_input().split())

print numpy.zeros(tuple(n), dtype=numpy.int)

print numpy.ones(tuple(n), dtype=numpy.int)
