import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
queue.append((0, 0))
n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수
maps = [[0] * n for _ in range(n)]
for i in range(k):      # 사과의 위치
    r, c = map(int, input().split())
    maps[r-1][c-1] = 1
l = int(input())    # 뱀의 방향 변환 횟수
snake_move = {}
for i in range(l):
    x, c = input().split()
    snake_move[int(x)] = c

r, c = 0, 0     # 뱀의 위치
time = 0    # 시간
pos = 0     # 뱀이 바라보는 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
length = 1      # 뱀의 길이
while True:
    if time in snake_move:
        if snake_move[time] == 'L':
            pos = (pos - 1) % 4
        else:
            pos = (pos + 1) % 4

    if r < 0 or r >= n or c < 0 or c >= n:      # 모서리 벗어나면 종료
        print(time)
        sys.exit()

    if maps[r][c] == 1:     # 사과가 있으면 뱀 길이 증가
        maps[r][c] = 0
        length += 1

    for i in range(length):
        x1, y1 = list(queue)[i]
        if r+dx[pos] == x1 and c+dy[pos] == y1:     # 자기 자신과 만나면 종료
            print(time+1)
            sys.exit()

    r += dx[pos]
    c += dy[pos]
    queue.appendleft((r, c))
    time += 1