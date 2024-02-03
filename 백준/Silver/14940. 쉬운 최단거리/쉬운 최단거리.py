import sys
sys.setrecursionlimit(10**6)
from collections import deque
n, m = map(int, input().split())    # 세로, 가로
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x1, y1 = queue.popleft()
        for k in range(4):
            nx = x1 + dx[k]
            ny = y1 + dy[k]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x1][y1] + 1
                queue.append((nx, ny))

    for p in range(n):
        for q in range(m):
            if matrix[p][q] == 1:
                matrix[p][q] = -1

    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 0:
            matrix[nx][ny] = 1

state = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            matrix[i][j] = 0
            bfs(i, j)
            state = True
            break
    if state:
        break

for i in matrix:
    print(*i)