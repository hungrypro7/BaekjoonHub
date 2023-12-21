import sys
input = sys.stdin.readline
n = int(input())
temp = 1
for i in range(1, n+1):
    temp *= i
cnt = 0
for j in str(temp)[::-1]:
    if j != '0':
        break
    cnt += 1
print(cnt)