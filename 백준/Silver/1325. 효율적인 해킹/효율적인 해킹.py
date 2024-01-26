import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    visited = [0] * n
    queue = deque()
    queue.append(x)
    visited[x] = 1
    co = 1
    while queue:
        y = queue.popleft()
        for j in com[y]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)
                co += 1
    return co

n, m = map(int, input().split())
com = [[] for _ in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    com[e-1].append(s-1)

max_l = 0
ans = []
for i in range(n):
    count = bfs(i)
    if count > max_l:
        max_l = count
        ans = [i+1]
    elif count == max_l:
        ans.append(i+1)
print(*ans)