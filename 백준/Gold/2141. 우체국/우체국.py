import sys
input = sys.stdin.readline
n = int(input())
pos = []
peo = 0
for i in range(n):
    x, a = map(int, input().split())
    pos.append([x, a])  # 위치, 사람수
    peo += a
pos.sort()
st = peo / 2
temp = 0
ans = -10e10
for i in range(n):
    temp += pos[i][1]
    if temp >= st:
        ans = pos[i][0]
        break
print(ans)