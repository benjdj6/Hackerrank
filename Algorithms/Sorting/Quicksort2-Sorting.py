#!/bin/python
def quickSort(ar): 
    if len(ar) < 2:
        return ar
    if len(ar) == 2:
        if ar[0] > ar[1]:
            temp = ar[1]
            ar[1] = ar[0]
            ar[0] = temp
        print "{0} {1}".format(ar[0], ar[1])   
        return ar
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
    sub = quickSort(left) + equal + quickSort(right)
    for j in sub:
        print j,
    print ''
    return sub

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)