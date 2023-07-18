import sys
input = sys.stdin.readline
n, k = map(int, input().split())
height = list(map(int, input().split()))
d = [0]
for i in range(1, n):
    d.append(height[i] - height[i-1])
d.sort()
ans = 0
for i in range(1, n-k+1):
    ans += d[i]
print(ans)