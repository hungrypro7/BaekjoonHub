import sys
from collections import deque
m, n = map(int, input().split())    # 가로, 세로
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

bfs()

ans = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit()
    ans = max(ans, max(tomato[i]))

print(ans-1)