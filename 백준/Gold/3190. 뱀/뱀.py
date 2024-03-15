import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
queue.append((0, 0))
n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수
maps = [[0] * n for _ in range(n)]
for i in range(k):      # 사과의 위치
    r, c = map(int, input().split())
    maps[r-1][c-1] = 2

l = int(input())    # 뱀의 방향 변환 횟수
snake_move = {}
for i in range(l):
    x, c = input().split()
    snake_move[int(x)] = c

r, c = 0, 0     # 뱀의 위치
time = 0    # 시간
pos = 0     # 뱀이 바라보는 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maps[r][c] = 1
while True:
    r += dx[pos]
    c += dy[pos]
    time += 1

    if time in snake_move:
        if snake_move[time] == 'L':
            pos = (pos - 1) % 4
        else:
            pos = (pos + 1) % 4

    if r < 0 or r >= n or c < 0 or c >= n:      # 모서리 벗어나면 종료
        print(time)
        sys.exit()

    if maps[r][c] == 2:     # 사과가 있으면 뱀 길이 증가
        maps[r][c] = 1
        queue.append((r, c))
    elif maps[r][c] == 0:   # 사과가 없을 때
        maps[r][c] = 1      # 뱀이 있는 자리를 1
        queue.append((r, c))
        x1, y1 = queue.popleft()
        maps[x1][y1] = 0    # 원래 뱀이 있던 자리에 없게 되므로 0
    else:   # 뱀이 있는 자리를 만나면
        print(time)
        sys.exit()