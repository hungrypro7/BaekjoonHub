n = int(input())
seq = list(map(int, input().split()))
dp = [0 for _ in range(n)]
cnt = 0
for i in range(n):
    if i > 0:
        dp[i] = max(dp[i-1]+seq[i], seq[i])
    else:
        dp[i] = seq[i]
print(max(dp))