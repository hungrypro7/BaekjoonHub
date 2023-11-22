import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    a, b = input().split()
    data.append([int(a), i, b])
data.sort()
for j in data:
    print(j[0], j[2])