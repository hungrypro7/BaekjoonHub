s = input()
zero, one = 0, 0
for i in s:
    if i == '0':
        zero += 1
    else:
        one += 1
print('0' * (zero//2), end='')
print('1' * (one//2), end='')