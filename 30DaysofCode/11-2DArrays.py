#!/bin/python

arr = []
hg_max = 0
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)
for i in range(2, 6):
    for j in range(2, 6):
        hg_sum = arr[i - 2][j - 2] + arr[i - 2][j - 1] + arr[i - 2][j]
        hg_sum += arr[i - 1][j - 1]
        hg_sum += arr[i][j - 2] + arr[i][j - 1] + arr[i][j]
        if hg_sum > hg_max or (i == 2 and j == 2):
            hg_max = hg_sum

print hg_max
