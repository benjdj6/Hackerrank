# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
a = set(map(int, raw_input().split()))
n = int(raw_input())
b = set(map(int, raw_input().split()))
print len(a.intersection(b))
