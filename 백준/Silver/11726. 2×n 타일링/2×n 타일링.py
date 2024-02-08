import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 1, 2]
if n > 2:
    for i in range(n-2):
        dp.append(dp[-1]+dp[-2])
print(dp[n] % 10007)