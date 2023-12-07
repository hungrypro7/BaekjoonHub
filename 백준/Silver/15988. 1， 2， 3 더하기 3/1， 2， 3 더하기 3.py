import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
test = []
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(n):
    a = int(input())
    test.append(a)
for i in range(4, 1000001):
    dp[i] = (dp[i-3] % 1000000009) + (dp[i-2] % 1000000009) + (dp[i-1] % 1000000009)
for j in test:
    print(dp[j] % 1000000009)