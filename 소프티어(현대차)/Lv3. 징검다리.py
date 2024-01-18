import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
rock = [1] * n
for i in range(n):
    m = 0
    for j in range(i):
        if heights[i] > heights[j]:
            m = max(m, rock[j])
    rock[i] += m
print(max(rock))