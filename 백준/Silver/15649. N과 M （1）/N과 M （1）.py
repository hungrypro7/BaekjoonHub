from itertools import permutations
n, m = map(int, input().split())
temp = [i for i in range(1, n+1)]
a = permutations(temp, m)
for i in list(a):
    print(*i)
