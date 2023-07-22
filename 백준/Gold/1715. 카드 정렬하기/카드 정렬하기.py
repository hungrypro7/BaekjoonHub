import sys
import heapq
input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
ans = 0
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    temp = a + b
    ans += temp
    heapq.heappush(cards, temp)
print(ans)