import sys
input = sys.stdin.readline
n = int(input())
sg_card = list(map(int, input().split()))
sg_card.sort()
d = dict()
for i in sg_card:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = int(input())
sols = list(map(int, input().split()))
ans = [0] * (m)
for i, sol in enumerate(sols):
    left = 0
    right = len(sg_card) - 1
    while left <= right:
        mid = (left + right) // 2
        if sg_card[mid] > sol:
            right = mid - 1
        elif sg_card[mid] < sol:
            left = mid + 1
        else:
            ans[i] = d[sg_card[mid]]
            break
print(*ans)