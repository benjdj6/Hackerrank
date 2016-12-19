s = int(raw_input().strip())
memo = {1: 1, 2: 2, 3: 4}


def upstairs(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = upstairs(n - 1) + upstairs(n - 2) + upstairs(n - 3)
        return memo[n]


for a0 in xrange(s):
    n = int(raw_input().strip())
    print upstairs(n)
