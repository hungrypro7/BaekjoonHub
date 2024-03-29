import sys
input = sys.stdin.readline
m, n = map(int, input().split())
print(2 * min(m, n) - 1 - (m <= n))