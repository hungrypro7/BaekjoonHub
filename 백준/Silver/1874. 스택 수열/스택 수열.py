import sys
input = sys.stdin.readline
n = int(input())
seq = []    # 수열이 들어있는 배열
for i in range(n):
    seq.append(int(input()))
ans = []
stack = []
p = 1
while seq:  # 수열이 다 비면 break
    if stack and stack[-1] == seq[0]:
        stack.pop()
        del seq[0]
        ans.append('-')
    else:
        stack.append(p)
        p += 1
        ans.append('+')
        if n+1 < p:
            print('NO')
            sys.exit(0)
for i in ans:
    print(i)