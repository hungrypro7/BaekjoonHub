import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = a[:]
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            dp[i] = max(dp[j]+a[i], dp[i])
print(max(dp))