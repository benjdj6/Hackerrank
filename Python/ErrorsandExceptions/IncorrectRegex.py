# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(raw_input())
for i in range(t):
    try:
        re.compile(raw_input())
        print True
    except:
        print False
