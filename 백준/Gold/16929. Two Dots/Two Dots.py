import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
dot = []
for i in range(n):
    dot.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
def dfs(x, y, count):
    global ans
    visited[x][y] = 1
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and dot[x+dx[i]][y+dy[i]] == alp:
            if x+dx[i] == ch1 and y+dy[i] == ch2 and count >= 3:
                ans = 1
                return
            elif not visited[x+dx[i]][y+dy[i]]:
                dfs(x+dx[i], y+dy[i], count+1)

for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        ch1, ch2 = i, j
        alp = dot[i][j]
        dfs(i, j, 0)
        if ans == 1:
            print("Yes")
            sys.exit(0)
print("No")