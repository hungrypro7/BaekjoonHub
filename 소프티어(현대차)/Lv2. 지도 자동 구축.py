import sys
input = sys.stdin.readline
n = int(input())
dp = [0]
dp2 = [3]
for i in range(n):
    dp.append(dp2[i]**2)
    dp2.append(dp2[-1]+dp2[-1]-1)

print(dp[n])