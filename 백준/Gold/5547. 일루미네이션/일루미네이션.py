from collections import deque
w, h = map(int, input().split())
build = []
build.append([0] * (w+2))
for i in range(h):
    build.append([0] + list(map(int, input().split())) + [0])
build.append([0] * (w+2))

dx1 = [-1, -1, 0, 0, 1, 1]   # x가 짝수일 때 육각형 방향
dy1 = [0, 1, -1, 1, 0, 1]

dx2 = [-1, -1, 0, 0, 1, 1]      # x가 홀수일 때 육각형 방향
dy2 = [-1, 0, -1, 1, -1, 0]
count = 0
def bfs(x, y):
    global count
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x1, y1 = queue.popleft()
        if x1 % 2 == 0:
            for i in range(6):
                nx = x1 + dx2[i]
                ny = y1 + dy2[i]
                if 0 <= nx < h+2 and 0 <= ny < w+2:
                    if build[nx][ny] == 0 and not visited[nx][ny]:      # 0일 때는 이동
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                    if build[nx][ny] == 1:      # 1일 때는 모서리 하나 추가
                        count += 1
        else:
            for i in range(6):
                nx = x1 + dx1[i]
                ny = y1 + dy1[i]
                if 0 <= nx < h+2 and 0 <= ny < w+2:
                    if build[nx][ny] == 0 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                    if build[nx][ny] == 1:
                        count += 1

visited = [[0] * (w+2) for _ in range(h+2)]
bfs(0, 0)

print(count)