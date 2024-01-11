import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
sys.setrecursionlimit(10**6)
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    check[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            return check[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                queue.append((nx, ny))

for i in range(t):
    I = int(input())    # 한 변의 길이
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    check = [[0] * I for _ in range(I)]
    ans = bfs(x1, y1)
    print(ans)