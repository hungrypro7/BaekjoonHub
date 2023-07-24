import sys
input = sys.stdin.readline
n, x = map(int, input().split())
visitor = list(map(int, input().split()))
count = []
ans = sum(visitor[:x])
count.append(ans)
temp = sum(visitor[:x])
for i in range(x, n):
    temp -= visitor[i-x]
    temp += visitor[i]
    if temp >= ans:
        count.append(temp)
        ans = temp
if ans == 0:
    print('SAD')
    sys.exit()
print(ans)
print(count.count(ans))
