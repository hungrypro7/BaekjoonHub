import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for i in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)
    if 2 in temp:
        x = i   # 목표지점 x, y
        y = temp.index(2)
visited = [[-1] * m for j in range(n)]
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
def BFS(x1, y1):
    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = 0     # 목표 지점 방문 기록
    while queue:

        (ax1, ay1) = queue.popleft()

        for i in range(4):
            a, b = ax1+nx[i], ay1+ny[i]
            if 0 <= a < n and 0 <= b < m and visited[a][b] == -1:
                if maps[a][b] == 1:
                    queue.append((a, b))
                    visited[a][b] = visited[ax1][ay1] + maps[a][b]
                elif maps[a][b] == 0:
                    visited[a][b] = 0
BFS(x, y)
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and maps[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()