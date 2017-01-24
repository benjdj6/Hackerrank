#!/bin/python


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print " ".join(map(str, arr[::-1]))
