import sys
import copy
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())    # 세로, 가로 크기
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    global ans
    mp = copy.deepcopy(maps)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if mp[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and mp[nx][ny] == 0:
                mp[nx][ny] = 2
                queue.append((nx, ny))

    temp = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] == 0:
                temp += 1
    ans = max(temp, ans)

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1      # 벽 세우기
                wall(cnt+1)
                maps[i][j] = 0

wall(0)
print(ans)