# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
nums = [0] * 100
for i in range(n):
    curr = int(raw_input().split(' ')[0])
    nums[curr] += 1
run_total = 0
for i in range(100):
    run_total += nums[i]
    print run_total,
