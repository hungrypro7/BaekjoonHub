import sys
input = sys.stdin.readline
e, s, m = map(int, input().split())
for i in range(10000000):
    if (i % 15)+1 == e and (i % 28)+1 == s and (i % 19)+1 == m:
        print(i+1)
        break
