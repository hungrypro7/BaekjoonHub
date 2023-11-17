tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
ans = ''
while n != 0:
    ans += tmp[n % b]
    n //= b
print(ans[::-1])