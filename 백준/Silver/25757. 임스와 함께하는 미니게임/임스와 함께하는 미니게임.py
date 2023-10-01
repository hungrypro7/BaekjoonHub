import sys
input = sys.stdin.readline
n, game = input().split()
n = int(n)
p = set()
for i in range(n):
    inp = input()
    p.add(inp)

ans = 0
if game == 'Y':
    ans = len(p)
elif game == 'F':
    ans = len(p) // 2
elif game == 'O':
    ans = len(p) // 3

print(ans)