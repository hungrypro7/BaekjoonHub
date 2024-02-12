import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())     # 가로, 세로, 상자 수
box = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    box.append(temp)

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            queue.append((nz, nx, ny))

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                sys.exit(0)
        ans = max(ans, max(box[i][j]))
print(ans-1)