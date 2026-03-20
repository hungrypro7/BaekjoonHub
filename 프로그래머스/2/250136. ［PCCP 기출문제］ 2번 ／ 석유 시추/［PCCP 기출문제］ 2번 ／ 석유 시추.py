from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, land):
    queue = deque([(x, y)])
    visited[x][y] = 1

    amount = 1
    cols = set([y])

    while queue:
        ix, iy = queue.popleft()

        for k in range(4):
            nx = ix + dx[k]
            ny = iy + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    amount += 1
                    cols.add(ny)

    return amount, cols

def solution(land):
    global n, m, visited
    n, m = len(land), len(land[0])

    visited = [[0] * m for _ in range(n)]
    oil_by_col = [0] * m

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                amount, cols = bfs(i, j, land)
                for col in cols:
                    oil_by_col[col] += amount

    return max(oil_by_col)