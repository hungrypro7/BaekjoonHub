from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
not_mix = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    not_mix[x-1][y-1] = 1     # 섞어 먹으면 안 되는 조합
    not_mix[y-1][x-1] = 1

kinds = [i for i in range(1, n+1)]
ice_cream = list(combinations(kinds, 3))
ans = 0
for j in ice_cream:
    if not_mix[j[0]-1][j[1]-1] or not_mix[j[1]-1][j[2]-1] or not_mix[j[0]-1][j[2]-1]:
        continue
    else:
        ans += 1
print(ans)