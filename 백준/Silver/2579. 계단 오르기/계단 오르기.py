import sys
input = sys.stdin.readline
n = int(input())    # 계단의 개수
dp = [0] * 300
steps = [0] * 300
for i in range(n):
    steps[i] = int(input())
dp[0] = steps[0]
dp[1] = steps[1] + steps[0]
dp[2] = steps[2] + max(steps[0], steps[1])
for i in range(3, n):
    dp[i] = max(steps[i]+steps[i-1]+dp[i-3], steps[i]+dp[i-2])
print(dp[n-1])