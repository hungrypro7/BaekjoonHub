import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
dp2 = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
ans = [0] * n
for i in range(n):
    ans[i] = dp[i]+dp2[i]
print(max(ans)-1)