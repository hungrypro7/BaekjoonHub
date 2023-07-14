n = int(input())
buildings = list(map(int, input().split()))
ans = 0
for i, j in enumerate(buildings):       # index, 원소
    can_see = 0
    if i < n-1:      # 오른쪽 탐색
        can_see += 1
        inclination = buildings[i+1] - j
        for k in range(i+2, n):
            if (buildings[k] - j) / (k-i) > inclination:
                can_see += 1
            inclination = max((buildings[k] - j) / (k-i), inclination)
    if i >= 1:
        can_see += 1
        inclination = j - buildings[i-1]
        for k in range(i-2, -1, -1):
            if (j - buildings[k]) / (i-k) < inclination:
                can_see += 1
            inclination = min((j - buildings[k]) / (i-k), inclination)
    ans = max(ans, can_see)
print(ans)