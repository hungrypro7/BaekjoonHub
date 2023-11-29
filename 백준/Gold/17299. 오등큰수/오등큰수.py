import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
ans = [-1] * n
f = [0] * 1000001
stack = []
for i in seq:
    f[i] += 1
for i in range(n):
    while stack and f[seq[stack[-1]]] < f[seq[i]]:
        ans[stack.pop()] = seq[i]
    stack.append(i)
print(*ans)