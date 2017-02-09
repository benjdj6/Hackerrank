import numpy

a = numpy.array(map(float, raw_input().split()), float)
print numpy.floor(a)
print numpy.ceil(a)
print numpy.rint(a)
