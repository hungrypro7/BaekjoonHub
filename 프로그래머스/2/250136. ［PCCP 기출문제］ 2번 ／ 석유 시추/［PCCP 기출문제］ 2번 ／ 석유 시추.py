from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    col_oil = [0] * m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True

        size = 1
        cols = set([y])   # 이 덩어리가 포함하는 열들

        while queue:
            cx, cy = queue.popleft()

            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        size += 1
                        cols.add(ny)

        return size, cols

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size, cols = bfs(i, j)
                for col in cols:
                    col_oil[col] += size

    return max(col_oil)