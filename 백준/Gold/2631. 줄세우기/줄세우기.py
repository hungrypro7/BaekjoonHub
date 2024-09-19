n = int(input())    # 아이들의 수
line = []
dp = [1] * n
for i in range(n):
    line.append(int(input()))
for i in range(n):
    temp = 0
    for j in range(i-1, -1, -1):
        if line[j] < line[i]:
            temp = max(temp, dp[j])
    dp[i] += temp

print(n - max(dp))