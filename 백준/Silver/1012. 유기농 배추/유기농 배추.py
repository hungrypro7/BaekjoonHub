import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def DFS(a, b):
    global cabbage, count
    cabbage[a][b] = 0
    if 0 <= a-1 <= n-1 and cabbage[a-1][b] == 1:
        DFS(a-1, b)
    if 0 <= a+1 <= n-1 and cabbage[a+1][b] == 1:
        DFS(a+1, b)
    if 0 <= b-1 <= m-1 and cabbage[a][b-1] == 1:
        DFS(a, b-1)
    if 0 <= b+1 <= m-1 and cabbage[a][b+1] == 1:
        DFS(a, b+1)

ans = []
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    count = 0
    for p in range(n):
        for q in range(m):
            if cabbage[p][q] == 1:
                DFS(p, q)
                count += 1
    ans.append(count)

for i in ans:
    print(i)