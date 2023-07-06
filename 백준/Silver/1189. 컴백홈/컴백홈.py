import sys
sys.setrecursionlimit(10000)
r, c, k = map(int, input().split())
path = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0
def DFS(x, y, depth):
    global count

    if not visited[x][y]:
        visited[x][y] = True

    if x == 0 and y == c-1:
        if depth == k-1:
            count += 1
            return
        else:
            return

    if depth > k-1:
        return

    if x > 0 and not visited[x-1][y] and path[x-1][y] != 'T':   # 위쪽
        DFS(x-1, y, depth+1)
        visited[x-1][y] = False

    if y < c-1 and not visited[x][y+1] and path[x][y+1] != 'T':   # 오른쪽
        DFS(x, y+1, depth+1)
        visited[x][y+1] = False

    if x < r-1 and not visited[x+1][y] and path[x+1][y] != 'T':   # 아래쪽
        DFS(x+1, y, depth+1)
        visited[x+1][y] = False

    if y > 0 and not visited[x][y-1] and path[x][y-1] != 'T':  # 왼쪽
        DFS(x, y-1, depth+1)
        visited[x][y-1] = False

DFS(r-1, 0, 0)
print(count)