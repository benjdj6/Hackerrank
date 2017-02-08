import numpy

n, m = map(int, raw_input().split())
arr = []
for i in range(n):
    arr.append(map(int, raw_input().split()))

arr = numpy.array(arr)
print numpy.transpose(arr)
print arr.flatten()
