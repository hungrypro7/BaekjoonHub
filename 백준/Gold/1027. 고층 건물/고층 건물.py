n = int(input())
building = list(map(int, input().split()))
max_see = 0
for i in range(n):
    temp_see = 0
    if n-i >= 2:
        async1 = building[i+1] - building[i]
        temp_see += 1
        for j in range(i+2, n):   # 오른쪽 탐색
            if 1.0 * (building[j] - building[i]) / (j-i) <= async1:
                continue
            async1 = 1.0 * (building[j] - building[i]) / (j-i)
            temp_see += 1
    if i > 0:
        async2 = building[i] - building[i-1]
        temp_see += 1
        for k in range(i-2, -1, -1):
            if 1.0 * (building[i] - building[k]) / (i-k) >= async2:
                continue
            async2 = 1.0 * (building[k] - building[i]) / (k - i)
            temp_see += 1
    max_see = max(max_see, temp_see)

print(max_see)