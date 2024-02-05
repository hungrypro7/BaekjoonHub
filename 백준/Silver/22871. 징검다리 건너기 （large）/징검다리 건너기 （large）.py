import math
n = int(input())
stones = list(map(int, input().split()))
dp = [0] + [math.inf] * (n-1)
for i in range(1, n):
    for j in range(i):
        temp = max((i-j)*(1+abs(stones[i]-stones[j])), dp[j])
        dp[i] = min(temp, dp[i])
print(dp[-1])