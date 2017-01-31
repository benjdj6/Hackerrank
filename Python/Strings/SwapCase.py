# Enter your code here. Read input from STDIN. Print output to STDOUT
ls = list(raw_input())
result = []
for char in ls:
    if char.isupper():
        result.append(char.lower())
    else:
        result.append(char.upper())
print ''.join(result)
