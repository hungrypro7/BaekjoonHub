import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
ans = [-1] * n
stack = []
for i in range(n):
    while stack and seq[stack[-1]] < seq[i]:
        ans[stack.pop()] = seq[i]
    stack.append(i)
print(*ans)