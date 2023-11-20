import sys
n = int(input())
x, y = [], []
min_x, min_y, max_x, max_y = 0, 0, 0, 0
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
min_x = min(x)
min_y = min(y)
max_x = max(x)
max_y = max(y)
print((max_x-min_x) * (max_y-min_y))