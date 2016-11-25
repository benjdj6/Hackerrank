# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    prices = map(int, raw_input().split())
    localMax = 0;
    profit = 0;
    for j in range(n-1,-1,-1):
        if prices[j] >= localMax:
            localMax = prices[j]
        profit += localMax - prices[j]
    print profit