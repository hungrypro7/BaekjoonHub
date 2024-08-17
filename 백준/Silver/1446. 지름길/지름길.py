n, d = map(int, input().split())    # 지름길 개수, 고속도로 길이
info = []
for i in range(n):
    info.append(list(map(int, input().split())))
info.sort()    # 정렬
dp = [i for i in range(d+1)]    # 거리별

k = 0
for i in range(d+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    while k < n:
        if i == info[k][0]:
            if info[k][1] <= d:    # 해당 지점에 도달했을 때 & 목표 지점 도달 전
                dp[info[k][1]] = min(dp[i]+info[k][2], dp[info[k][1]])    # 최단거리 dp vs 원래 dp
            k += 1    # 지름길 개수보다 작을 때
        else:
            break

print(dp[d])