import sys
from itertools import product
input = sys.stdin.readline
n, k = map(int, input().split())
k_ele = list(map(str, input().split()))
temp = len(str(n))
while True:
    tep = list(product(k_ele, repeat=temp))
    ans = []
    for i in tep:
        if int("".join(i)) <= n:
            ans.append(int("".join(i)))

    if ans:
        print(max(ans))
        sys.exit(0)
    else:
        temp -= 1