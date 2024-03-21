import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())    # 세로, 가로 크기
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
visited = [[0] * m for _ in range(n)]
def dfs(x, y, score, count):
    global ans
    score += paper[x][y]

    if count == 3:
        ans = max(ans, score)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, score, count+1)
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, 0)
        visited[i][j] = 0

# ㅗ
for i in range(1, n):
    for j in range(m-2):
        ans = max(ans, paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+1])

# ㅏ
for i in range(n-2):
    for j in range(m-1):
        ans = max(ans, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1])

# ㅜ
for i in range(n-1):
    for j in range(m-2):
        ans = max(ans, paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1])

# ㅓ
for i in range(n-2):
    for j in range(1, m):
        ans = max(ans, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j-1])
print(ans)