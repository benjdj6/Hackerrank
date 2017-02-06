# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(t):
    try:
        a, b = map(int, raw_input().split())
        print a / b
    except ZeroDivisionError as e:
        print "Error Code:", e
    except ValueError as e:
        print "Error Code:", e
