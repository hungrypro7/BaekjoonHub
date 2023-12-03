stack = []
s = input()
for i in range(len(s)):
    stack.append(s[i:])
stack.sort()
for i in stack:
    print(i)