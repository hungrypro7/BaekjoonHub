from collections import deque
import sys
N, M = map(int, input().split())
list = sys.stdin.readline().split()
count = 0
d = deque([i for i in range(1, N+1)])

for i in list:
    state = True
    while(state):
        if int(i) == d[0]:      # 왼쪽 끝에 원소가 있을 때
            d.popleft()
            state = False
        elif int(i) == d[-1]:   # 오른쪽 끝에 원소가 있을 때
            d.pop()
            count += 1
            state = False
        else:
            left = False
            for j in range(len(d)//2+1):
               if d[j] == int(i):
                   left = True
            if left:        # 왼쪽으로 회전
                d.rotate(-1)
                count += 1
            else:           # 오른쪽으로 회전
                d.rotate(1)
                count += 1
print(count)