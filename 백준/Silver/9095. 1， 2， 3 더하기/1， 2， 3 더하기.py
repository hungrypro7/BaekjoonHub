t = int(input())
dp = [0, 1, 2, 4]
for i in range(4, 12):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
for i in range(t):
    print(dp[int(input())])