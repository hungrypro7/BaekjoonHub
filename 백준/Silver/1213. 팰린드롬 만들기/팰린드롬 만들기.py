import sys
str = input()
alp = [0] * 26
for i in str:
    alp[ord(i)-65] += 1
count = 0
for j in alp:
    if j % 2 == 1:
        count += 1
if count > 1:
    print('I\'m Sorry Hansoo')
    sys.exit(0)
ans = []
state = False
for i in range(26):
    if alp[i] % 2 == 0:
        for j in range(alp[i]):
            ans.insert(len(ans)//2, chr(i+65))
    else:
        a = alp[i]-1
        b = chr(i+65)
        state = True
        for j in range(a):
            ans.insert(len(ans)//2, chr(i+65))
if state:
    ans.insert(len(ans)//2, b)
ans = ''.join(ans)
print(ans)