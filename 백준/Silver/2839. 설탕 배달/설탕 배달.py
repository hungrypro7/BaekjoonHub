import sys
input = sys.stdin.readline
n = int(input())
dp = []
while n != 0:
    if (n >= 5 and n % 5 == 0) or (n-5)%3 == 0:
        dp.append(5)
        n -= 5
    elif (n >= 3 and n % 3 == 0) or n > 10:
        dp.append(3)
        n -= 3
    else:
        print(-1)
        sys.exit(0)
print(len(dp))