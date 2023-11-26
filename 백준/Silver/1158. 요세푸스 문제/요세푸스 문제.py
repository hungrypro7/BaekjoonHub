n, k = map(int, input().split())
yos = [i for i in range(1, n+1)]
p = 0
ans = []
while yos:
    p = (p + k - 1) % len(yos)
    ans.append(str(yos.pop(p)))
print('<', ', '.join(ans), '>', sep='')