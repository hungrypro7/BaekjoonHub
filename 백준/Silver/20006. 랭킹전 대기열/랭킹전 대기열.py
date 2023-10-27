import sys
import heapq
input = sys.stdin.readline
p, m = map(int, input().split())
data = []
for i in range(p):
    l, n = input().split()
    if data:
        for idx, j in enumerate(data):
            if j[0]-10 <= int(l) <= j[0]+10 and len(j[1]) < m:
                heapq.heappush(j[1], (n, int(l)))
                break
            elif idx == len(data)-1:
                data.append((int(l), []))
                heapq.heappush(data[-1][1], (n, int(l)))
                break
    else:
        data.append((int(l), []))
        heapq.heappush(data[-1][1], (n, int(l)))

for j in data:
    if len(j[1]) == m:
        print("Started!")
        while j[1]:
            a = heapq.heappop(j[1])
            print(a[1], a[0])
    else:
        print("Waiting!")
        while j[1]:
            a = heapq.heappop(j[1])
            print(a[1], a[0])