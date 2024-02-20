from itertools import permutations
n = int(input())
k = int(input())
card = []
for i in range(n):
    card.append(str(input()))
ans = []
per = list(permutations(card, k))
for i in per:
    temp = ''
    for j in i:
        temp += j
    if temp not in ans:
        ans.append(temp)
print(len(ans))