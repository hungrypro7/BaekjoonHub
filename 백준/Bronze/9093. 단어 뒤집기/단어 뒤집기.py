t = int(input())
for i in range(t):
    stack = []
    a = list(input().split())
    for j in a:
        stack.append(j)
    for j in stack:
        print(j[::-1], end=' ')
    print()