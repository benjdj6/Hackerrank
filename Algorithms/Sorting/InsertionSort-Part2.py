#!/bin/python
def insertionSort(ar):    
    for i in range(0, len(ar)):
        if i < len(ar) - 1:
            if ar[i] > ar[i+1]:
                for j in range(i+1,0,-1):
                    if ar[j] < ar[j-1]:
                        temp = ar[j-1]
                        ar[j-1] = ar[j]
                        ar[j] = temp
                    else:
                        break
            for n in ar:
                print n,
            print ""
                        
                    

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)