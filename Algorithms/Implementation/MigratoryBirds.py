#!/bin/python

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
birds = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for b in types:
    birds[b] += 1
max_b = -1
common = -1
for key, val in birds.iteritems():
    if val > max_b or (val == max_b and key < common):
        max_b = val
        common = key
print common
