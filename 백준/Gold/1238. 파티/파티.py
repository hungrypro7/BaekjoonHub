import heapq
import math
n, m, x = map(int, input().split())    # 학생 수, 도로 개수, 파티를 벌일 마을
roads = [[] for _ in range(n+1)]
ans = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in roads[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

for i in range(m):
    start, end, time = map(int, input().split())
    roads[start].append((end, time))

dis = [math.inf] * (n+1)
dijkstra(x)    # 파티가 벌어지는 마을에서 dijkstra

for i in range(1, n+1):
    ans[i] = dis[i]

for j in range(1, n+1):
    if j == x:
        continue
    dis = [math.inf] * (n + 1)
    dijkstra(j)
    ans[j] += dis[x]

print(max(ans))