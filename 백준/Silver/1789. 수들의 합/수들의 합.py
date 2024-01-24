import sys
input = sys.stdin.readline
n = int(input())
temp = 0
if n <= 2:
    print(1)
elif n == 3:
    print(2)
for i in range(1, n):
    temp += i
    if temp > n:
        print(i-1)
        sys.exit(0)