from collections import deque
n, m = map(int, input().split())    # 세로, 가로 크기
pic = []
for i in range(n):
    pic.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0    # 방 개수
width = 0    # 방 넓이
def bfs(a, b):
    global width, visited
    visited[a][b] = 1
    q = deque()
    q.append((a, b))
    temp = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and pic[nx][ny] and (not visited[nx][ny]):
                q.append((nx, ny))
                visited[nx][ny] = 1
                temp += 1
    width = max(width, temp)

for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            count += 1

print(count)
print(width)