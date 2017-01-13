# Enter your code here. Read input from STDIN. Print output to STDOUT
i, j, k = raw_input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]
total = 0
for x in range(i, j + 1):
    rev = int(str(x)[::-1])
    if abs(x - rev) % k == 0:
        total += 1
print total
