import math
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    mv = 1e9
    for j in range(1, int(math.sqrt(i))+1):
        mv = min(mv, dp[i-j**2])
    dp[i] = mv+1
print(dp[-1])