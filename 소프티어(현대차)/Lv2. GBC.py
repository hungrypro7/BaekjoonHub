import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # 각 구간 길이, 테스트 구간 길이
ran = []
for i in range(n):
    len, speed = map(int, input().split())
    ran.append([len, speed])

inspect = []
for i in range(m):
    len, speed = map(int, input().split())
    inspect.append([len, speed])

temp = 0  # 현재 검사하는 구간
p, q = 0, 0  # 구간 번째
ans = 0
while temp < 100:
    if temp == ran[p][0]:
        ran[p+1][0] += ran[p][0]
        p += 1
    if temp == inspect[q][0]:
        inspect[q+1][0] += inspect[q][0]
        q += 1
    if ran[p][1] < inspect[q][1]:
        ans = max(ans, abs(ran[p][1] - inspect[q][1]))
    temp += 1
print(ans)
