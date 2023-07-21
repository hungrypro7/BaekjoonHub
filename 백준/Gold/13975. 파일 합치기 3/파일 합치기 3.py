import heapq
t = int(input())
for i in range(t):
    k = int(input())
    pages = list(map(int, input().split()))
    ans = 0
    pages.sort()
    while len(pages) != 1:
        a = heapq.heappop(pages)
        b = heapq.heappop(pages)
        temp = a + b
        heapq.heappush(pages, temp)
        ans += temp
    print(ans)