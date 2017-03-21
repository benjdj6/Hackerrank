#!/bin/python


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
count = 0
for x in range(max(a), min(b) + 1):
    good = True
    for i in a:
        if x % i != 0:
            good = False
            break
    if good:
        for j in b:
            if j % x != 0:
                good = False
                break
    if good:
        count += 1
print count
