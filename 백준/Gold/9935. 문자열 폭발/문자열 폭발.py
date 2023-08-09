import sys
word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
for i in range(len(word)):
    stack.append(word[i])
    if stack[-len(bomb):] == list(bomb):
        for j in range(len(bomb)):
            stack.pop()
if len(stack) > 0:
    ans = ''.join(_ for _ in stack)
    print(ans)
else:
    print('FRULA')