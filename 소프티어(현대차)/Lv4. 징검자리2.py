import sys
import bisect
input = sys.stdin.readline
n = int(input())    # 돌의 개수
stones = list(map(int, input().split()))    # 돌 높이

min_to_max = [1] * n
temp = [stones[0]]
for i in range(n):
    if stones[i] > temp[-1]:
        temp.append(stones[i])
    else:
        idx = bisect.bisect_left(temp, stones[i])
        temp[idx] = stones[i]
    min_to_max[i] = len(temp)

max_to_min = [1] * n
temp = [stones[-1]]
for i in range(n-1, -1, -1):
    if stones[i] > temp[-1]:
        temp.append(stones[i])
    else:
        idx = bisect.bisect_left(temp, stones[i])
        temp[idx] = stones[i]
    max_to_min[i] = len(temp)

ans = 0
for i in range(n):
    ans = max(ans, min_to_max[i]+max_to_min[i])
print(ans-1)
