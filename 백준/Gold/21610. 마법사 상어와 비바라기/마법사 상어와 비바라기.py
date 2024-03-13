import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # 격자 크기, 이동 정보
basket = []
for i in range(n):      # 비의 양
    basket.append(list(map(int, input().split())))
move = []    # 방향 & 이동 칸수
cloud = [[0] * n for _ in range(n)]  # 구름을 저장하는 용도
for i in range(m):      # 이동 m번
    d, s = map(int, input().split())
    move.append((d, s))

# 이동 방향 1 ~ 8
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# 첫 번째 구름 생성
cloud[n-2][0], cloud[n-2][1], cloud[n-1][0], cloud[n-1][1] = 1, 1, 1, 1
for i in range(m):
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    direct, size = move[i][0], move[i][1]
    temp = []
    for j in range(n):
        for k in range(n):
            if cloud[j][k] == 1:
                cloud[j][k] = 0
                nx = (j + dx[direct] * size) % n
                ny = (k + dy[direct] * size) % n
                temp.append((nx, ny))

    for j in temp:
        cloud[j[0]][j[1]] = 1

    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for j in range(n):
        for k in range(n):
            if cloud[j][k] == 1:
                basket[j][k] += 1

    # 3. 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    for j in range(n):
        for k in range(n):
            if cloud[j][k] == 1:
                temp_count = 0
                for l in range(2, 9, 2):    # 대각선 4방향 조회
                    if 0 <= j+dx[l] < n and 0 <= k+dy[l] < n and basket[j+dx[l]][k+dy[l]] > 0:
                        temp_count += 1
                basket[j][k] += temp_count

    # 4. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for j in range(n):
        for k in range(n):
            if cloud[j][k] != 1 and basket[j][k] >= 2:
                cloud[j][k] = 1
                basket[j][k] -= 2
            elif cloud[j][k] == 1:
                cloud[j][k] = 0

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
ans = 0
for i in range(n):
    for j in range(n):
        ans += basket[i][j]
print(ans)