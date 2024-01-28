import sys
sys.setrecursionlimit(10**6)
n = int(input())
mp = []
for i in range(n):
    mp.append(list(map(int, input())))

def dfs(x, y):
    global cnt
    cnt += 1
    mp[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < n and mp[nx][ny]:
            dfs(nx, ny)

count = 0
ans = []
for i in range(n):
    for j in range(n):
        if mp[i][j] == 1:
            cnt = 0
            dfs(i, j)
            count += 1
            ans.append(cnt)

print(count)
ans.sort()
for i in ans:
    print(i)