import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())     # 로봇 청소기 x 좌표, y 좌표, 바라보는 방향
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))

cleaned_room = 0
dx = [1, 0, -1, 0]      # 하, 좌, 상, 우
dy = [0, -1, 0, 1]
direct = ['북', '동', '남', '서']   # 북, 동, 남, 서
dx2 = [-1, 0, 1, 0]
dy2 = [0, 1, 0, -1]
see = d         # 로봇이 바라보는 방향
visited = [[0] * m for _ in range(n)]

while True:
    if pos[r][c] == 0 and not visited[r][c]:      # 1 현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소한다.
        visited[r][c] = 1       # 청소
        cleaned_room += 1

    state = False
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m and pos[nx][ny] == 0 and not visited[nx][ny]:    # 3 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            state = True
            see -= 1        # 반시계 방향으로 90도 회전
            if see < 0:
                see = 3

            if 0 <= r + dx2[see] < n and 0 <= c + dy2[see] < m and pos[r + dx2[see]][c + dy2[see]] == 0 and not visited[r + dx2[see]][c + dy2[see]]:    # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
                r += dx2[see]
                c += dy2[see]
            break

    if not state:       # 3 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if 0 <= r+dx[see] < n and 0 <= c+dy[see] < m and pos[r+dx[see]][c+dy[see]] == 0:      # 바라보는 방향을 유지한 채로 1칸 후진할 수 있다면 1칸 후진
            r += dx[see]
            c += dy[see]
            continue
        else:
            print(cleaned_room)     # 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
            sys.exit()

print(cleaned_room)