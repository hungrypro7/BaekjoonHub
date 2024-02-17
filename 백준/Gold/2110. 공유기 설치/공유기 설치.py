import sys
input = sys.stdin.readline
n, c = map(int, input().split())
home = []
for i in range(n):
    home.append(int(input()))
home.sort()
s, e = 1, home[-1] - home[0]    # 공유기를 놓을 수 있는 최소 거리, 최대 거리

while s <= e:
    temp = 0    # 출발점
    mid = (s + e) // 2
    distance = 10000000001
    count = 1  # 공유기 설치 가능 개수
    for i in range(1, n):
        if home[i] - home[temp] >= mid:
            count += 1
            distance = min(distance, home[i]-home[temp])
            temp = i

    if count >= c:
        s = mid + 1
        ans = distance
    elif count < c:
        e = mid - 1

print(ans)