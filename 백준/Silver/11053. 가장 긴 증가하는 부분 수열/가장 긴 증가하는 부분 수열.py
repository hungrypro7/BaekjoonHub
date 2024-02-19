import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    temp = 0
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            temp = max(temp, dp[j])
    dp[i] += temp
print(max(dp))