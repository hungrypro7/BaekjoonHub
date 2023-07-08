n, m = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = cost[0][i]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 0) or (j == m-1 and k == 2):
                dp[i][j][k] = 1000000
            elif k == 0:
                dp[i][j][0] = cost[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
            elif k == 1:
                dp[i][j][1] = cost[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
            elif k == 2:
                dp[i][j][2] = cost[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

result = 1000000
for i in dp[-1]:
    for j in i:
        result = min(result, j)
print(result)