import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())    # 세로 격자, 가로 격자
ice = []
ice.append([0] * (m+2))
for i in range(n):
    ice.append([0] + list(map(int, input().split())) + [0])
ice.append([0] * (m+2))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hour = 0
def bfs(x, y):
    global hour
    queue = deque()
    queue.append((x, y))
    visited = [[0] * (m+2) for _ in range(n+2)]
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < n+2 and 0 <= ny < m+2:
                if ice[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1     # 방문 여부 저장
                    queue.append((nx, ny))
                elif ice[nx][ny] == 1:      # 얼음 있으면 집어 넣음
                    visited[nx][ny] += 1

    for i in range(n+2):
        for j in range(m+2):
            if visited[i][j] >= 2:
                ice[i][j] = 0

    hour += 1
    for i in range(n+2):      # 탈출 조건 확인
        if 1 in ice[i]:
            return bfs(0, 0)
    return

for i in range(n+2):
    if 1 in ice[i]:
        bfs(0, 0)
print(hour)
