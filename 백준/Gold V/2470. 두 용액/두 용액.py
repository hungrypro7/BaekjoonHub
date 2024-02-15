import sys
import math
input = sys.stdin.readline
n = int(input())
wa = list(map(int, input().split()))
wa.sort()
p, q = 0, n-1
total = [0, 0]
st = math.inf
while p < q:
    if abs(wa[p] + wa[q]) <= st:
        st = abs(wa[p]+wa[q])
        total[0] = wa[p]
        total[1] = wa[q]

    if wa[p] + wa[q] > 0:
        q -= 1
    elif wa[p] + wa[q] < 0:
        p += 1
    else:
        break

print(*total)