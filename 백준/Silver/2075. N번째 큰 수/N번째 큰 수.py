import sys
import heapq
input = sys.stdin.readline
n = int(input())
pq = []
for i in range(n):
    num = list(map(int, input().split()))
    if len(pq) != n:
        for j in num:
            heapq.heappush(pq, j)
    else:
        for j in num:
            if pq[0] < j:
                heapq.heappush(pq, j)
                heapq.heappop(pq)
print(pq[0])