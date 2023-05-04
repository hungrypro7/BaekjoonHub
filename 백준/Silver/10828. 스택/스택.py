import sys
N = int(input())
stack = []
for i in range(N):
    input = sys.stdin.readline().split()
    if input[0] == 'push':
        stack.append(input[1])
    elif input[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif input[0] == 'size':
        print(len(stack))
    elif input[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif input[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)