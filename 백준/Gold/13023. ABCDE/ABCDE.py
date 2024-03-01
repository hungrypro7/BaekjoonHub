import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n)]
visited = [False] * n
arrive = False

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[now] = False

for j in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for k in range(n):
    DFS(k, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)