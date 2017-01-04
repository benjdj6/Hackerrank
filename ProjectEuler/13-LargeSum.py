# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
sum = 0
for i in range(n):
    sum += int(raw_input())
print ''.join(list(str(sum))[0:10])