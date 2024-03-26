import sys
import copy
input = sys.stdin.readline
r, c, t = map(int, input().split())     # 행, 열, t초
room = []
for i in range(r):
    room.append(list(map(int, input().split())))

# 1. 미세먼지 확산
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while t != 0:
    visited = [[0] * c for _ in range(r)]
    air_cleaner = []
    # 미세먼지 존재 위치 파악
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                visited[i][j] = 1
            elif room[i][j] == -1:   # 공기청정기 위치
                air_cleaner.append((i, j))
    room2 = copy.deepcopy(room)

    # 확산
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 1:
                temp = int(room2[i][j] / 5)
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        room[nx][ny] += temp
                        room[i][j] -= temp

    # 2. 공기청정기 작동
    # 윗부분
    for i in range(air_cleaner[0][0]-1, -1, -1):
        if room[i+1][0] == -1:
            continue
        else:
            room[i+1][0] = room[i][0]
            room[i][0] = 0

    for i in range(1, c):
        room[0][i-1] = room[0][i]
        room[0][i] = 0

    for i in range(1, air_cleaner[0][0]+1):
        room[i-1][-1] = room[i][-1]
        room[i][-1] = 0

    for i in range(c-2, 0, -1):
        room[air_cleaner[0][0]][i+1] = room[air_cleaner[0][0]][i]
        room[air_cleaner[0][0]][i] = 0

    # 아랫부분
    for i in range(air_cleaner[1][0]+1, r):
        if room[i-1][0] == -1:
            continue
        else:
            room[i-1][0] = room[i][0]
            room[i][0] = 0

    for i in range(1, c):
        room[-1][i-1] = room[-1][i]
        room[-1][i] = 0

    for i in range(r-2, air_cleaner[1][0]-1, -1):
        room[i+1][-1] = room[i][-1]
        room[i][-1] = 0

    for i in range(c-2, 0, -1):
        room[air_cleaner[1][0]][i+1] = room[air_cleaner[1][0]][i]
        room[air_cleaner[1][0]][i] = 0

    t -= 1

ans = 0
for i in room:
    ans += sum(i)
print(ans+2)