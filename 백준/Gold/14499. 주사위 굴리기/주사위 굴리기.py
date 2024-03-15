import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())      # 세로, 가로, x, y, 명령의 개수
maps = []
dice = [0, 0, 0, 0, 0, 0]   # 주사위
for i in range(n):
    maps.append(list(map(int ,input().split())))
order = list(map(int, input().split()))     # 이동하는 명령
dx = [0, 0, -1, 1]     # 동, 서, 북, 남
dy = [1, -1, 0, 0]
for i in range(k):
    nx = x + dx[order[i]-1]
    ny = y + dy[order[i]-1]
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
        if order[i] == 1:  # 동쪽
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif order[i] == 2:    # 서쪽
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif order[i] == 3:    # 북쪽
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif order[i] == 4:    # 남쪽
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if maps[x][y] != 0:
            dice[-1] = maps[x][y]       # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
            maps[x][y] = 0
        else:
            maps[x][y] = dice[-1]       # 이동한 칸에 쓰여 있는 수가 0인 경우
        print(dice[0])      # 윗면에 적혀있는 수 출력