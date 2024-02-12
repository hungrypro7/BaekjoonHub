import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        count += int(K / coins[i])
        K %= coins[i]

print(count)