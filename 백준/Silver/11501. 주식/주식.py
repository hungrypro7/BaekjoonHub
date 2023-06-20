import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    benefit = 0
    max = 0
    for i in stock:
        if max < i:
            max = i
        elif max > i:
            benefit += max - i
    print(benefit)