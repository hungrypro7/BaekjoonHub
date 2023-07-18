import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    judge = []
    for j in range(n):
        docu, inter = map(int, input().split())
        judge.append([docu, inter])
    judge.sort()
    ans = 1
    temp = judge[0][1]
    for j in range(1, n):
        if judge[j][1] < temp:
            ans += 1
            temp = judge[j][1]
    print(ans)