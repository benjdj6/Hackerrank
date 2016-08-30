# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
def quickSort(ar):
    if len(ar) < 2:
        return ar
    index = 0
    pivot = ar[len(ar)-1]
    for i in range(0, len(ar)-1):
        if ar[i] < pivot:
            temp = ar[index]
            ar[index] = ar[i]
            ar[i] = temp
            index += 1
    ar[len(ar)-1] = ar[len(ar)/2]
    ar[len(ar)/2] = pivot
    right = len(ar)/2+1
    ar = quickSort(ar[0:len(ar)/2]) + [pivot] + quickSort(ar[right:len(ar)])
    return ar
    

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print quickSort(ar)