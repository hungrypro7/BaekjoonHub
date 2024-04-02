import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())        # 세로, 가로
office = []
cctv = []
for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([office[i][j], i, j])
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]]

# 북 남 서 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fill(board, mode, x, y):
    for i in mode:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = -1
def dfs(depth, board):
    global ans
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += board[i].count(0)
        ans = min(ans, cnt)
        return

    temp = copy.deepcopy(board)
    num, x, y = cctv[depth]
    for i in mode[num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)

ans = 1e10
dfs(0, office)
print(ans)