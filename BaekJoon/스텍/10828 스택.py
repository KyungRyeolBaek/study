import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    inputs = sys.stdin.readline().split()
    command = inputs[0]
    if command == 'push':
        stack.append(inputs[1])
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
