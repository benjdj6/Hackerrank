from itertools import product

A = map(int, raw_input().split(' '))
B = map(int, raw_input().split(' '))
for x in list(product(A, B)):
    print x,
