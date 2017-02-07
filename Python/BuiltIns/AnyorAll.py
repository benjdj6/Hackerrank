# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = map(int, raw_input().split())
print all(i > 0 for i in arr) and any(str(i) == str(i)[::-1] for i in arr)
