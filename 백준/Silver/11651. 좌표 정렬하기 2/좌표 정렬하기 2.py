import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([b, a])
data.sort()
for j in data:
    print(j[1], j[0])