import sys
import itertools
input = sys.stdin.readline
# 도시 크기, 폐업시키지 않을 치킨집 최대 개수
n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append((i, j))
        elif maps[i][j] == 1:
            home.append((i, j))

chicken = list(itertools.combinations(chicken, m))
ans = 10000000
for i in chicken:
    temp = 0
    for p, q in home:   # 집 좌표
        a = 1000000
        for j, k in i:  # 치킨 집 좌표
            a = min(abs(p-j)+abs(q-k), a)
        temp += a
    ans = min(temp, ans)
print(ans)