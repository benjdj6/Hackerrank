# Enter your code here. Read input from STDIN. Print output to STDOUT
str = raw_input()
l = list(str)
arg = raw_input()
arg = arg.split()
i = int(arg[0])
l[i] = arg[1]
str = ''.join(l)
print str