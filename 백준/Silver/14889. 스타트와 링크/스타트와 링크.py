from itertools import combinations
import sys
n = int(sys.stdin.readline())
skill = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
num = [i for i in range(1, n+1)]
sub = 1000000000
for i in combinations(num, n//2):
    k = set(num) - set(i)
    skill1, skill2 = 0, 0
    for j in combinations(i, 2):
        skill1 += skill[j[0]-1][j[1]-1] + skill[j[1]-1][j[0]-1]
    for j in combinations(k, 2):
        skill2 += skill[j[0]-1][j[1]-1] + skill[j[1]-1][j[0]-1]
    temp = abs(skill1 - skill2)
    sub = min(sub, temp)

print(sub)