import sys
sys.setrecursionlimit(10**6)
n = int(input())
map = []
for i in range(n):
    map.append(list(input()))

def dfs(x, y):
    global count
    count += 1
    map[x][y] = '0'
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == '1':
            dfs(nx, ny)

ans = 0
ans_count = []
for i in range(n):
    for j in range(n):
        if map[i][j] == '1':
            ans += 1
            count = 0
            dfs(i, j)
            ans_count.append(count)

print(ans)
ans_count.sort()
for i in ans_count:
    print(i)