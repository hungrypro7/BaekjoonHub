import sys
input = sys.stdin.readline
n, m = map(int, input().split())
screen = []
for i in range(n):
    screen.append(int(input()))

mi, ma = min(screen), max(screen) * m
ans = ma
while mi <= ma:
    mid = (mi+ma) // 2
    total = 0
    for i in screen:
        total += mid // i

    if total >= m:
        ma = mid - 1
        ans = min(ans, mid)
    elif total < m:
        mi = mid + 1

print(ans)