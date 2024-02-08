import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 1, 3]
if n > 2:
    for i in range(n-2):
        dp.append((2*dp[-2])+dp[-1])
print(dp[n]%10007)