t = int(input())    # 테스트 케이스 개수
for i in range(t):
    n = int(input())
    dp = []
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])
    ans = max(dp[0][-1], dp[1][-1])
    print(ans)