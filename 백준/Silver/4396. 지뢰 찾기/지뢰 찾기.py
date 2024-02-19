n = int(input())
mine_map = []
for i in range(n):
    mine_map.append(list(input()))
map = []
for i in range(n):
    map.append(list(input()))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
state = False
for i in range(n):
    for j in range(n):
        if map[i][j] == 'x' and mine_map[i][j] == '.':
            count = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and mine_map[nx][ny] == '*':
                    count += 1
            map[i][j] = count
        elif map[i][j] == 'x' and mine_map[i][j] == '*':
            map[i][j] = '*'
            state = True

if state:
    for i in range(n):
        for j in range(n):
            if mine_map[i][j] == '*':
                map[i][j] = '*'

for i in map:
    print(*i, sep='')