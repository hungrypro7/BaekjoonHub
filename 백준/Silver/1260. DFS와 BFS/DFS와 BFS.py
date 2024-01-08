import sys
from collections import deque

input = sys.stdin.readline

n, m, start = map(int, input().split())
A = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n+1):
    A[i].sort()

def DFS(now):
    print(now, end=' ')
    visited[now] = True
    for j in A[now]:
        if not visited[j]:
            DFS(j)

visited = [False] * (n+1)
DFS(start)

def BFS(now):
    queue = deque()
    queue.append(now)
    visited[now] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for j in A[v]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)

print()
visited = [False] * (n+1)
BFS(start)