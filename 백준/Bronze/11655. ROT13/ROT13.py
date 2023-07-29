s = input()
for i in s:
    if ord(i) >= 110 and ord(i) <= 122:
        temp = 122 - ord(i)
        print(chr(97+(12-temp)), end='')
    elif ord(i) >= 97 and ord(i) <= 109:
        print(chr(ord(i)+13), end='')
    elif ord(i) >= 65 and ord(i) <= 77:
        print(chr(ord(i) + 13), end='')
    elif ord(i) >= 78 and ord(i) <= 90:
        temp = 90 - ord(i)
        print(chr(65+(12-temp)), end='')
    else:
        print(i, end='')