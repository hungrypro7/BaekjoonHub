s = input()
num = [0, 0]
temp = s[0]
if temp == '0':
    num[0] += 1
else:
    num[1] += 1
for i in range(1, len(s)):
    if s[i] != temp:
        if s[i] == '0':
            num[0] += 1
        else:
            num[1] += 1
        temp = s[i]
print(min(num))