import itertools
n, m = map(int, input().split())
chicken = []
for i in range(n):
    chicken.append(list(map(int, input().split())))

ans = 0
for i, j, k in itertools.combinations(range(m), 3):
    temp = 0
    for p in range(n):
        temp += max(chicken[p][i], chicken[p][j], chicken[p][k])
    ans = max(temp, ans)

print(ans)