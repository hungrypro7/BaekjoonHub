import sys
input = sys.stdin.readline
from collections import deque
dec = deque([])
n = int(input())
for i in range(n):
    mov = list(input().split())
    if mov[0] == 'push_front':
        dec.appendleft(mov[1])
    elif mov[0] == 'push_back':
        dec.append(mov[1])
    elif mov[0] == 'pop_front':
        if dec:
            print(dec.popleft())
        else:
            print(-1)
    elif mov[0] == 'pop_back':
        if dec:
            print(dec.pop())
        else:
            print(-1)
    elif mov[0] == 'size':
        print(len(dec))
    elif mov[0] == 'empty':
        if dec:
            print(0)
        else:
            print(1)
    elif mov[0] == 'front':
        if dec:
            print(dec[0])
        else:
            print(-1)
    elif mov[0] == 'back':
        if dec:
            print(dec[-1])
        else:
            print(-1)