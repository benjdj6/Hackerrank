#!/bin/python

known = {1: 1, 2: 2}


def factorial(n):
    if n not in known:
        known[n] = n * factorial(n - 1)
        return known[n]
    return known[n]


print factorial(int(raw_input().strip()))
