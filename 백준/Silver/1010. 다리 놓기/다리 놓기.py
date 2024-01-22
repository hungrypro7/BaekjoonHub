import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    s, e = map(int, input().split())
    dp = [0]
    dp[0] = e
    for j in range(1, s):
        dp.append(dp[-1]*(e-j)//(j+1))
    print(dp[s-1])