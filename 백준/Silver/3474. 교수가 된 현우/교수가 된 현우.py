import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = 1
    count = 0
    while True:
        a *= 5
        if a > n:
            break
        count += 1
    ans = 0
    for j in range(1, count+1):
        ans += n // (5 ** j)
    print(ans)