import heapq
n = int(input())
heap = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(heap, (a, b))
while heap:
    a = heapq.heappop(heap)
    print(*a)