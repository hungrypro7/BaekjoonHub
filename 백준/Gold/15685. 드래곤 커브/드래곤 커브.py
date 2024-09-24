import sys
input = sys.stdin.readline
n = int(input())    # 커브 개수
matrix = [[0] * 101 for _ in range(101)]    # 좌표

dx = [0, -1, 0, 1]    # 좌 하 우 상
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split())    # 드래곤 커브의 시작 점 x y, 시작 방향 d, 세대 g
    matrix[x][y] = 1

    curve = [d]
    for j in range(g):
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    for j in curve:
        x += dx[j]
        y += dy[j]
        if 0 <= x < 101 and 0 <= y < 101:
            matrix[x][y] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:    # 네 꼭짓점이 모두 드래곤 커브이면
            ans += 1

print(ans)