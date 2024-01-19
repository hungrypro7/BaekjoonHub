import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())    # 컴퓨터의 수
p = int(input())    # 컴퓨터 쌍의 수
comp = [[] for _ in range(n)]
for i in range(p):
    s, e = map(int, input().split())
    comp[s-1].append(e-1)
    comp[e-1].append(s-1)

def dfs(num):
    global count
    count += 1
    visited[num] = 1
    for j in comp[num]:
        if visited[j] == 0:
            dfs(j)

visited = [0] * n
count = 0
dfs(0)
if count == 0:
    print(count)
else:
    print(count-1)