isStrictSuper = "True"
A = set(map(int, raw_input().split()))
n = int(raw_input())
for i in range(n):
    s = set(map(int, raw_input().split()))
    if s.issuperset(A) or s == A or not A.issuperset(s):
        isStrictSuper = "False"
        break
print isStrictSuper
