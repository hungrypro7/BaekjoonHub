import sys
input = sys.stdin.readline
n = int(input())
table = [0] * (n+1)
for i in range(1, n+1):
    table[i] = int(input())

def dfs(node):
    global start
    visited[node] = 1
    if not visited[table[node]]:
        return dfs(table[node])
    if table[node] == start:
        return True

    return False

check = [0] * (n+1)
ans = []
for i in range(1, n+1):
    start = i
    visited = [0] * (n + 1)
    if dfs(i) and not check[i]:
        for j in range(n+1):
            if visited[j] == 1:
                ans.append(j)
                check[j] = 1

print(len(ans))
ans.sort()
for i in ans:
    print(i)