import sys
input = sys.stdin.readline
p = int(input())
for i in range(p):
    inp = list(map(int, input().split()))
    ans = 0
    a = [inp[1]]
    for j in inp[2:]:
        for p in range(len(a)):
            if a[p] > j:
                ans += len(a) - p
                a.insert(p, j)
                break
            elif p == len(a)-1:
                a.append(j)
    print(inp[0], ans)