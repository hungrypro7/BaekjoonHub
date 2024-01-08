import sys
sys.setrecursionlimit(10**6)
n = int(input())
maps = []
for i in range(n):
    maps.append(list(input()))

def DFS(x, y):
    global connect
    connect += 1
    maps[x][y] = '0'

    if x-1 >= 0 and maps[x-1][y] != '0':
        DFS(x-1, y)
    if x+1 < n and maps[x+1][y] != '0':
        DFS(x+1, y)
    if y-1 >= 0 and maps[x][y-1] != '0':
        DFS(x, y-1)
    if y+1 < n and maps[x][y+1] != '0':
        DFS(x, y+1)

ans = []
count = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] != '0':
            connect = 0
            DFS(i, j)
            ans.append(connect)
            count += 1

print(count)
ans.sort()
for i in ans:
    print(i)