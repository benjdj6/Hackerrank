# Enter your code here. Read input from STDIN. Print output to STDOUT
#Not accurate to enough decimal places, causes test failure at extremely high values
import math

param = raw_input().split()
length = int(param[0])
s1 = int(param[1])
s2 = int(param[2])
diff = abs(s1 - s2)

i = int(raw_input())
for j in range(i, 0, -1):
    q = int(raw_input())
    print float((math.sqrt(2) * (length - float(math.sqrt(q))))/diff)