#!/bin/python
def partition(ar): 
    left = []
    equal = []
    right = []
    for i in ar:
        if i == ar[0]:
            equal.append(i)
        elif i < ar[0]:
            left.append(i)
        else:
            right.append(i)
    for j in left:
        print j,
    for k in equal:
        print k,
    for l in right:
        print l,
            

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)