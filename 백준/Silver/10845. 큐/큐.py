import sys
input = sys.stdin.readline
from collections import deque
queue = deque([])
n = int(input())
for i in range(n):
    com = list(input().split())
    if com[0] == 'push':
        queue.appendleft(com[1])
    elif com[0] == 'pop':
        if queue:
            a = queue.pop()
            print(a)
        else:
            print('-1')
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if queue:
            print('0')
        else:
            print(1)
    elif com[0] == 'front':
        if queue:
            print(queue[-1])
        else:
            print('-1')
    elif com[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print('-1')