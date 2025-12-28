n = int(input())
INF = 10**9
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[n] if dp[n] != INF else -1)
