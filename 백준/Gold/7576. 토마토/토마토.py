import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
tomatos = []
for i in range(n):
    tomatos.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = tomatos[x][y] + 1
            queue.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 0:
            print(-1)
            sys.exit(0)
    ans = max(ans, max(tomatos[i]))
print(ans-1)