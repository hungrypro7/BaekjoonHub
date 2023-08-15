import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1

for i in graph:
    print(' '.join(str(s) for s in i))