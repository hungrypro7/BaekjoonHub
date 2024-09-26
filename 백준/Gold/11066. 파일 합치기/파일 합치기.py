import sys
import math
input = sys.stdin.readline
t = int(input())    # 테스트 케이스 개수

for i in range(t):
    k = int(input())    # 장수
    dp = [[0] * k for _ in range(k)]    # dp[i][j]를 i번째 파일부터 j번째 파일을 합쳤을 때 최솟값
    chapter = list(map(int, input().split()))    # 파일 크기

    for p in range(k):    # 두 파일 합치는 경우만 dp에 저장
        for q in range(k):
            if q - p == 1:
                dp[p][q] = chapter[p] + chapter[q]

    for p in range(k-2, -1, -1):    # 거꾸로 올라감
        for q in range(k):
            if dp[p][q] == 0 and p < q:
                dp[p][q] = min([dp[p][r] + dp[r+1][q] for r in range(p, q)]) + sum(chapter[p:q+1])

    print(dp[0][k-1])