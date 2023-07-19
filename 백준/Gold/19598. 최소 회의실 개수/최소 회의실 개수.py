import sys
import heapq
input = sys.stdin.readline
n = int(input())
meeting_room = []
for i in range(n):
    s, e = map(int, input().split())
    meeting_room.append([s, e])
meet = sorted(meeting_room)
a = []
heapq.heappush(a, meet[0][1])
for i in range(1, n):
    if meet[i][0] < a[0]:
        heapq.heappush(a, meet[i][1])
    else:
        heapq.heappop(a)
        heapq.heappush(a, meet[i][1])
print(len(a))