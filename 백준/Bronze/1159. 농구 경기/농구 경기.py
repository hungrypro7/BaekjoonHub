n = int(input())
alp = [0] * 26
for i in range(n):
    name = input()
    alp[ord(name[0])-97] += 1
state = True
for i in range(26):
    if alp[i] >= 5:
        print(chr(i+97), end='')
        state = False
if state:
    print('PREDAJA')