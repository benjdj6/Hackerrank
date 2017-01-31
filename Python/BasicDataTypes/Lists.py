if __name__ == '__main__':
    N = int(raw_input())

l = []
for j in range(N):
    command = raw_input().split(' ')
    if command[0] == "insert":
        l.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        l.remove(int(command[1]))
    elif command[0] == "append":
        l.append(int(command[1]))
    elif command[0] == "sort":
        l.sort()
    elif command[0] == "pop":
        l.pop()
    elif command[0] == "reverse":
        l.reverse()
    else:
        print l
