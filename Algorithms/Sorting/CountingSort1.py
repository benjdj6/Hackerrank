# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
ar = map(int, raw_input().split())
count = [0]*100
for num in ar:
    count[num] += 1

for val in count:
    print val,