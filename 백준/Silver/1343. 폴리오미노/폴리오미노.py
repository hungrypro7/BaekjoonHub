board = list(map(str, input().split('.')))
state = True
for i in range(len(board)):
    valid = len(board[i])
    str = ''
    while(valid):
        if valid >= 4:
            str += 'AAAA'
            valid -= 4
            state = True
        elif valid >= 2:
            str += 'BB'
            valid -= 2
            state = True
        else:
            state = False
            valid = 0
    if not state:
        break
    board[i] = str

if state:
    print('.'.join(board))
else:
    print(-1)