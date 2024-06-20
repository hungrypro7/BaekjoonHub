import sys
n, m = map(int, input().split())  # 격자 크기, 칸의 수
matrix = []  # 격자
point = []  # 방문해야 할 지점
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(m):
    x, y = map(int, input().split())
    point.append((x-1, y-1))

ans = 0
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
a = []
def dfs(x, y, num):
    global ans
    a.append((x, y))
    if num == m - 1 and x == point[num][0] and y == point[num][1]:
        ans += 1
        return    # 함수 종료
    elif num < m - 1 and x == point[num][0] and y == point[num][1]:
        num += 1
        dfs(x, y, num)
        num -= 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0 and not visited[nx][ny]:
            visited[x][y] = 1
            dfs(nx, ny, num)
            visited[x][y] = 0

x1, y1 = point[0][0], point[0][1]
dfs(x1, y1, 1)
print(ans)
