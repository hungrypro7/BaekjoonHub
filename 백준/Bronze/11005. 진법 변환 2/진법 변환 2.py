import sys
n, b = map(int, input().split())
exp = 0   # 지수
temp = 1
if b == 10:
    print(n)
    sys.exit(0)
elif n < b:
    if n < 10:
        print(n)
    else:
        print(chr(n+55))
    sys.exit(0)
else:
    while n >= temp:
        temp *= b
        exp += 1
ans = [''] * exp
for i in range(exp):
    k = n // (b ** (exp - i - 1))
    if k >= 10:
        ans[i] = chr(k+55)
    else:
        ans[i] = str(k)
    n -= (b ** (exp - i - 1)) * k
for i in ans:
    print(i, end='')