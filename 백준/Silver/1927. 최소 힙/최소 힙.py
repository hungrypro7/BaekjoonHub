import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    data = int(input())
    if data == 0:
        if heap:
            a = heapq.heappop(heap)
            print(a)
        else:
            print(0)
    else:
        heapq.heappush(heap, data)