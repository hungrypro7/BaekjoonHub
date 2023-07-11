import sys
import copy
from itertools import permutations
input = sys.stdin.readline
n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
rotate = []
for _ in range(k):
    r1, s1, k1 = map(int, input().split())
    rotate.append([r1, s1, k1])
ans = int(1e9)

def rotate_array(row, col, ko):
    if ko == 0:
        return
    r1 = row - 1 - ko
    c1 = col - 1 - ko
    r2 = row - 1 + ko
    c2 = col - 1 + ko
    temp = []
    for i in range(c1, c2+1):       # 임시 배열에 원소 옮기기
        temp.append(q[r1][i])
    for i in range(r1+1, r2):
        temp.append(q[i][c2])
    for i in range(c2, c1-1, -1):
        temp.append(q[r2][i])
    for i in range(r2-1, r1, -1):
        temp.append(q[i][c1])

    idx = 0
    for j in range(c1+1, c2+1):
        q[r1][j] = temp[idx]
        idx += 1
    for j in range(r1+1, r2):
        q[j][c2] = temp[idx]
        idx += 1
    for j in range(c2, c1-1, -1):
        q[r2][j] = temp[idx]
        idx += 1
    for j in range(r2-1, r1-1, -1):
        q[j][c1] = temp[idx]
        idx += 1
    rotate_array(row, col, ko-1)

seq = tuple(permutations(rotate))

for i in seq:
    q = copy.deepcopy(array)
    for j in i:
        rotate_array(j[0], j[1], j[2])
    for k in q:
        ans = min(ans, sum(k))

print(ans)