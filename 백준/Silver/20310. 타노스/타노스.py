s = input()
zero, one = 0, 0
for i in s:
    if i == '0':
        zero += 1
    else:
        one += 1
for _ in range(zero//2):
    print(0, end='')
for _ in range(one//2):
    print(1, end='')