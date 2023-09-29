import sys
input = sys.stdin.readline
S = set([])
m = int(input())
for i in range(m):
    inp = input().split()
    order = inp[0]
    if len(inp) >= 2:
        num = int(inp[1])

    if order == 'add':
        if num in S:
            continue
        else:
            S.add(num)
    elif order == 'remove':
        if num in S:
            S.remove(num)
    elif order == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif order == 'all':
        S = set([i for i in range(1, 21)])
    elif order == 'empty':
        S = set([])