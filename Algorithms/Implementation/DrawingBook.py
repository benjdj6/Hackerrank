#!/bin/python


n = int(raw_input().strip())
p = int(raw_input().strip())
turns = (n / 2) - (p / 2)
if p % 2 == 1:
    turns = (n - p) / 2
print min(turns, (p / 2))
