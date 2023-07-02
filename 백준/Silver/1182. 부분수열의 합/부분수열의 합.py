from itertools import combinations, permutations
n, s = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
match = 0
for i in range(1, n+1):
    com = list(combinations(seq, i))
    for j in com:
        if sum(j) == s:
            match += 1
print(match)