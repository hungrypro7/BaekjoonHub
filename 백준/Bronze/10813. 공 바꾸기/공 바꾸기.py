import sys
input = sys.stdin.readline
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for k in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
print(*basket)