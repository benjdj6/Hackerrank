# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0
n, m = map(int, raw_input().split())
arr = map(int, raw_input().split())
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))

for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1
print happiness
