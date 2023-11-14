import sys
input = sys.stdin.readline
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for k in range(m):
    i, j = map(int, input().split())
    if i == 1:
        basket = basket[:i-1] + basket[j-1::-1] + basket[j:]
    else:
        basket = basket[:i-1] + basket[j-1:i-2:-1] + basket[j:]
print(*basket)