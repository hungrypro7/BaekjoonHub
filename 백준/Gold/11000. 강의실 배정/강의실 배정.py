import heapq
n = int(input())
time = []
for i in range(n):
    s, e = map(int, input().split())
    heapq.heappush(time, [s, e])

room = []
b = heapq.heappop(time)
heapq.heappush(room, b[1])

for i in range(1, n):
    a = heapq.heappop(time)
    if a[0] < room[0]:
        heapq.heappush(room, a[1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, a[1])

print(len(room))