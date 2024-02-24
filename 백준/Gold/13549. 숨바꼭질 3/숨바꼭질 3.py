from collections import deque
n, k = map(int, input().split())
Max = 100001
dist = [0] * Max
visited = [False] * Max
q = deque()
q.append(n)
visited[n] = True

while q:
    now = q.popleft()
    if now*2 < Max and visited[now*2] == False:
        q.appendleft(now*2)
        visited[now*2] = True
        dist[now*2] = dist[now]
    if now-1 >= 0 and visited[now-1] == False:
        q.append(now-1)
        visited[now-1] = True
        dist[now-1] = dist[now] + 1
    if now+1 < Max and visited[now+1] == False:
        q.append(now+1)
        visited[now+1] = True
        dist[now+1] = dist[now] + 1

print(dist[k])