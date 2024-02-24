from collections import deque
n, m, t = map(int, input().split())     # 가로, 세로, 시간 제한
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp = 100000
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            elif 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 2 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                temp = visited[nx][ny] + (n-nx-1) + (m-ny-1)
                visited[nx][ny] = 1

    if visited[n-1][m-1] == 0:
        return temp
    else:
        return min(visited[n-1][m-1], temp)

ans = bfs(0, 0)
if ans == 0:
    print("Fail")
else:
    if ans <= t:
        print(ans)
    else:
        print("Fail")