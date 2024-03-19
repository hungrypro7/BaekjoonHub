import sys
from collections import deque
input = sys.stdin.readline
h, w = map(int, input().split())    # 세로, 가로
robot_map = []
for i in range(h):
    robot_map.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    # 상 하 좌 우
direct = ['^', 'v', '<', '>']
chx = [2, -2, 0, 0]
chy = [0, 0, 2, -2]
visited = [[0] * w for _ in range(h)]
def bfs(x1, y1):
    visited[x1][y1] = 1
    queue = deque()
    queue.append((x1, y1))
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        if 0 <= nx < h and 0 <= ny < w and robot_map[nx][ny] == '#':
            print(direct[i])
            temp = i    # 방향 측정을 위한 임시 변수 (회전했는지 안했는지를 검사함)
            break

    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if robot_map[nx][ny] == '#' and not visited[nx][ny]:
                    count += 1    # 
                    visited[nx][ny] = 1
                    robot_map[nx][ny] = '.'
                    if count == 2 and (0 <= nx + chx[i] < h and 0 <= ny + chy[i] < w and visited[nx+chx[i]][ny+chy[i]] == 1):    # 지나왔던 경로 인
                        if temp != i:    # 회전하게 될 때
                            if temp == 0 and i == 2:
                                print('L', end='')
                            elif temp == 0 and i == 3:
                                print('R', end='')
                            elif temp == 1 and i == 2:
                                print('R', end='')
                            elif temp == 1 and i == 3:
                                print('L', end='')
                            elif temp == 2 and i == 0:
                                print('R', end='')
                            elif temp == 2 and i == 1:
                                print('L', end='')
                            elif temp == 3 and i == 0:
                                print('L', end='')
                            elif temp == 3 and i == 1:
                                print('R', end='')
                        count = 0
                        print('A', end='')    # 두 칸 전진하면 A 출력
                        temp = i
                    queue.append((nx, ny))

for i in range(h):
    for j in range(w):
        if robot_map[i][j] == '#':    # 시작점 찾기
            ct = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < h and 0 <= ny < w and robot_map[nx][ny] == '#':
                    ct += 1  
            if ct < 2:
                print(i+1, j+1)
                bfs(i, j)
