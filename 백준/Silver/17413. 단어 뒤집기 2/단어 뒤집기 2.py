import sys
input = sys.stdin.readline
s = input()
ans = ''
temp = ''
state = False
for i in s:
    if i == '<':
        ans += temp[::-1]
        temp = ''
        state = True
    if state:   # <..> 내에 있을 때
        temp += i
    else:       # <..> 밖에 있을 때
        if i == ' ':
            ans += temp[::-1] + ' '
            temp = ''
        elif i == '\n':
            ans += temp[::-1]
        else:
            temp += i
    if i == '>':
        ans += temp
        temp = ''
        state = False
print(ans)