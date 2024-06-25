import sys
from itertools import permutations
n, m = map(int, input().split())    # 격자 크기, 친구 수
matrix = []
friend = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(m):    # 각 친구의 위치 정
    x, y = map(int, input().split())
    friend.append((x-1, y-1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, depth, score, path):
    global mx_path, mx_score
    visited[x][y] = 1
    score += matrix[x][y]
    path.append((x, y))
    if depth == 3:
        if mx_score < score:
            mx_score = score
            mx_path = path[:]
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and ((nx, ny) not in temp_path):
            dfs(nx, ny, depth+1, score, path)
            visited[nx][ny] = 0
            path.pop()

per = list(permutations(friend, m))
ans = 0
for i in per:
    temp_path = []
    temp_score = 0
    for x, y in i:
        mx_score, mx_path = 0, []
        dfs(x, y, 0, 0, [])
        temp_path += mx_path
        temp_score += mx_score
    ans = max(ans, temp_score)
print(ans)
