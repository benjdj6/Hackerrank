def fib(a, b, n, i):
    tmp = 0
    if(i < n):
        i += 1
        tmp = (b**2) + a
        fib(b, tmp, n, i)
    else:
        print b

inp = list(raw_input().split())
a = int(inp[0])
b = int(inp[1])
n = int(inp[2])
fib(a,b,n,2)