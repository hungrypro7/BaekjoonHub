import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())  # 휴개소 개수, 더 지으려고 하는 휴게소 개수, 고속도로 길이
loc = [0] + list(map(int, input().split())) + [l]
loc.sort()
start, end = 1, l-1
ans = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n+2):
        if loc[i] - loc[i-1] >= mid:
            count += (loc[i]-loc[i-1]-1) // mid
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)