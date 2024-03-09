import sys
input = sys.stdin.readline
p, n = map(int, input().split())
virus = list(map(int, input().split()))

ans = virus[0]
for i in range(1, n):
    ans = (ans * p) % 1000000007
    ans += virus[i]
print(ans)
