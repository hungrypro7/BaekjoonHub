import sys
input = sys.stdin.readline
x = int(input())
n = int(input())    # 물건의 종류
check = 0
for i in range(n):
    a, b = map(int, input().split())
    check += a * b
if check == x:
    print("Yes")
else:
    print("No")