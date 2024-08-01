from collections import deque
n = int(input())
pic = []
for i in range(n):
    pic.append(list(input()))

visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b):
    visited[a][b] = 1
    q = deque()
    q.append((a, b))
    po = pic[a][b]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and pic[nx][ny] == po and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return

def bfs_blind(a, b):
    visited2[a][b] = 1
    q2 = deque()
    q2.append((a, b))
    po = pic[a][b]
    while q2:
        x, y = q2.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if pic[nx][ny] == po and not visited2[nx][ny]:
                    visited2[nx][ny] = 1
                    q2.append((nx, ny))
                elif po == 'R' and pic[nx][ny] == 'G' and not visited2[nx][ny]:
                    visited2[nx][ny] = 1
                    q2.append((nx, ny))
                elif po == 'G' and pic[nx][ny] == 'R' and not visited2[nx][ny]:
                    visited2[nx][ny] = 1
                    q2.append((nx, ny))
    return

color_weak_no = 0
color_weak_yes = 0
before = 'A'
before2 = 'A'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            before = pic[i][j]
            bfs(i, j)
            color_weak_no += 1
        if not visited2[i][j]:
            before2 = pic[i][j]
            bfs_blind(i, j)
            color_weak_yes += 1

print(color_weak_no, color_weak_yes)