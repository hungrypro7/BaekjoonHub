import sys
sys.setrecursionlimit(10**6)
n = int(input())
tree = [[] for _ in range(n+1)]

def find(start, now):
    for a, b in tree[start]:
        if visited[a] == -1:
            visited[a] = b + now
            find(a, visited[a])

for i in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])
    tree[c].append([p, w])

visited = [-1] * (n+1)
visited[1] = 0    # 루트 노드
find(1, 0)

start = visited.index(max(visited))
visited = [-1] * (n+1)
visited[start] = 0
find(start, 0)
print(max(visited))