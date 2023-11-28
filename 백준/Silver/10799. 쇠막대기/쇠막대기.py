s = input()
stack = []
ans = 0
temp = ''
for i in range(len(s)):
    if s[i] == '(':
        ans += 1
        stack.append(s[i])
    elif s[i] == ')':
        if temp == '(':
            ans -= 1
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
    temp = s[i]
print(ans)