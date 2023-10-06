import sys
input = sys.stdin.readline
n, taesoo, p = map(int, input().split())

if n != 0:
    scores = list(map(int, input().split()))
else:
    print(1)
    sys.exit(0)

rank = 1
ans = 0
for i, data in enumerate(scores):   # idx, data
    if i >= 1 and data < scores[i-1]:
        rank = i+1

    if taesoo > data:
        if rank > p:
            ans = -1
        else:
            ans = rank
        break
    elif taesoo == data:
        if rank >= p:
            ans = -1
        else:
            ans = rank
        if i < n-1 and taesoo > scores[i+1]:
            break

    if i == n-1:
        if n < p:
            if taesoo < scores[-1]:
                ans = n+1
            elif taesoo == scores[-1]:
                ans = rank
            else:
                ans = rank
        else:
            ans = -1

print(ans)