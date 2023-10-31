import sys
input = sys.stdin.readline
n = int(input())    # 기둥 개수
building = []
max_h = 0
for i in range(n):
    l, h = map(int, input().split())
    building.append((l, h))
    if h > max_h:
        max_h = h
building.sort()

ans = 0
cl1, ch1 = 0, 0   # 현재 높이
# 처음부터 max_l 까지
for i in range(n):
    if building[i][1] > ch1:
        ans += ch1 * (building[i][0]-cl1)
        cl1 = building[i][0]
        ch1 = building[i][1]
    if building[i][1] == max_h:
        cl1 = building[i][0]
        break

# 끝부터 max_l 까지
cl2, ch2 = 0, 0
for i in range(n-1, -1, -1):
    if building[i][1] > ch2:
        ans += ch2 * (cl2 - building[i][0])
        cl2 = building[i][0]
        ch2 = building[i][1]
    if building[i][1] == max_h:
        cl2 = building[i][0]
        break
ans += (cl2 - cl1 + 1) * max_h
print(ans)