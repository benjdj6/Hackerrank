# Enter your code here. Read input from STDIN. Print output to STDOUT
new = []
old = []


def enqueue(num):
    new.append(num)


def dequeue():
    swapStacks()
    old.pop()


def peek():
    swapStacks()
    print old[len(old) - 1]


def swapStacks():
    if not old:
        while new:
            old.append(new.pop())


q = int(raw_input())

for i in range(q):
    command = map(int, raw_input().split())
    if command[0] == 1:
        enqueue(command[1])
    elif command[0] == 2:
        dequeue()
    else:
        peek()
