n, b = input().split()
ans = 0
for i, s in enumerate(n):
    if 65 <= ord(s) <= 90:
        ans += (int(b) ** (len(n)-i-1)) * (ord(s) - 55)
    else:
        ans += (int(b) ** (len(n)-i-1)) * int(s)
print(ans)