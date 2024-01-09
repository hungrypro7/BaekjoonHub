import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def DFS(x, y):
    global w, h
    m[x][y] = 0
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    for i in range(8):
        if 0 <= x+dx[i] < h and 0 <= y+dy[i] < w and m[x+dx[i]][y+dy[i]] != 0:
            DFS(x+dx[i], y+dy[i])

while True:
    m = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit(0)

    for i in range(h):
        m.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] != 0:
                DFS(i, j)
                count += 1

    print(count)