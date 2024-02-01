import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

P.sort()
temp = 0
for i in range(n):
    temp += P[i]
    P[i] = temp

print(sum(P))