chess = []
visited = [[False] * 6 for _ in range(6)]

for i in range(36):
    visit = input()
    chess.append(visit)

state = False
for i in range(len(chess)):
    if len(chess) != 36:
        state = False
        break
    if i <= len(chess) - 2:
        if (abs(ord(chess[i][0])-ord(chess[i+1][0])) == 1 and abs(int(chess[i][1])-int(chess[i+1][1])) == 2) or (abs(ord(chess[i][0])-ord(chess[i+1][0])) == 2 and abs(int(chess[i][1])-int(chess[i+1][1])) == 1):
            x = ord(chess[i][0]) - 65   # A, B, C, D, E, F는 각각 0, 1, 2, 3, 4, 5에 대응됨
            y = int(chess[i][1]) - 1
            if visited[x][y]:
                state = False        # 중복 방문하는 경우
                break
            else:
                visited[x][y] = True
        else:
            state = False        # 나이트가 방문할 수 없는 경우
            break
    else:                                   # i가 마지막일 때
        if (abs(ord(chess[i][0])-ord(chess[0][0])) == 1 and abs(int(chess[i][1])-int(chess[0][1])) == 2) or (abs(ord(chess[i][0])-ord(chess[0][0])) == 2 and abs(int(chess[i][1])-int(chess[0][1])) == 1):
            x = ord(chess[i][0]) - 65   # A, B, C, D, E, F는 각각 0, 1, 2, 3, 4, 5에 대응됨
            y = int(chess[i][1]) - 1
            if visited[x][y]:
                state = False       # 중복 방문하는 경우
                break
            else:
                visited[x][y] = True
                state = True
        else:
            state = False

if state:
    print("Valid")
else:
    print("Invalid")