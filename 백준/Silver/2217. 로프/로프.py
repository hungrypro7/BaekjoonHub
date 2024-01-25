import sys
input = sys.stdin.readline
n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort()
ans = 0
for idx, j in enumerate(rope):
    if j * (n-idx) >= ans:
        ans = j * (n-idx)
print(ans)