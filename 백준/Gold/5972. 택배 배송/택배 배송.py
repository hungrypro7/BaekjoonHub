import math
import heapq
n, m = map(int, input().split())    # 헛간, 소들의 길 개수
maps = [[] for _ in range(n+1)]
dis = [math.inf] * (n+1)    # 거리 저장 배열

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)    # 거리, 현재 위치
        if dis[now] < d:    # 현재 거리가 더 크면
            continue
        for v, w in maps[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

dijkstra(1)
print(dis[n])