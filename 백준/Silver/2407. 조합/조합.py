import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [1]
for i in range(1, m+1):
    dp.append(dp[-1]*(n-i+1)//i)
print(dp[-1])