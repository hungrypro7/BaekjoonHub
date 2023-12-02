s = input()
ans = ''
for i in s:
    if 65 <= ord(i) <= 90:
        if ord(i) + 13 > 90:
            temp = (ord(i) + 13) % 90
            ans += chr(64 + temp)
        else:
            ans += chr(ord(i)+13)
    elif 97 <= ord(i) <= 122:
        if ord(i) + 13 > 122:
            temp = (ord(i) + 13) % 122
            ans += chr(96 + temp)
        else:
            ans += chr(ord(i)+13)
    else:
        ans += i
print(ans)