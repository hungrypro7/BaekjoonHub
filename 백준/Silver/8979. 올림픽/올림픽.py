import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = []
medal = []
for i in range(n):
    nation, gold, silver, copper = map(int, input().split())
    data.append((nation, gold, silver, copper))
    medal.append((gold * 100000000) + (silver * 10000) + (copper * 1))
medal = sorted(medal, reverse=True)
temp, ans = 0, 0
for j in data:
    if j[0] == k:
        temp = medal.index(((j[1] * 100000000) + (j[2] * 10000) + (j[3] * 1)))
        for k in range(temp, -1, -1):
            if medal[k] > ((j[1] * 100000000) + (j[2] * 10000) + (j[3] * 1)):
                ans += 1
        break
print(ans+1)