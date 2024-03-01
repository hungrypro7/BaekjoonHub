from queue import PriorityQueue
import sys
input = sys.stdin.readline
que = PriorityQueue()
V, E = map(int, input().split())
st = int(input())   # 시작 정점의 번호
ma = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    ma[u].append([v, w])
visited = [0] * (V+1)
ans = [sys.maxsize] * (V+1)
ans[st] = 0
que.put((0, st))

while que.qsize() > 0:
    cur = que.get()
    c = cur[1]
    if visited[c]:
        continue
    visited[c] = 1
    for i in ma[c]:
        next = i[0]
        value = i[1]
        if ans[next] > ans[c] + value:
            ans[next] = ans[c] + value
            que.put((ans[next], next))
for i in range(1, V+1):
    if ans[i] == sys.maxsize:
        print("INF")
    else:
        print(ans[i])