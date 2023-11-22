n = int(input())
x = list(map(int, input().split()))
a = list(sorted(set(x)))
inf = {}
for i in range(len(a)):
    inf[a[i]] = i
for i in x:
    print(inf[i], end=' ')