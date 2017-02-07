# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, raw_input().split())
marks = []
for i in range(x):
    marks.append(map(float, raw_input().split()))
marks = list(zip(*marks))
for m in marks:
    print sum(m) / x
