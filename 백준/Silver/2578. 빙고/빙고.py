import sys
bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))
call = []
for j in range(5):
    call += list(map(int, input().split()))
check = [[0] * 5 for _ in range(5)]

def down(x, y):     # x = 0 일 때
    count = 0
    for p in range(5):
        if check[p][y] == 1:
            count += 1
    if count == 5:
        return True
    return False

def right(x, y):    # y = 0 일 때
    count = 0
    for p in range(5):
        if check[x][p] == 1:
            count += 1
    if count == 5:
        return True
    return False

def right_down(x, y):    # x, y = 0, 0 일 때
    count = 0
    for p in range(5):
        if check[p][p] == 1:
            count += 1
    if count == 5:
        return True
    return False

def left_down(x, y):   # x, y = 0, 4 일 때
    count = 0
    for p in range(5):
        if check[p][4-p] == 1:
            count += 1
    if count == 5:
        return True
    return False

for k in range(25):
    ans_count = 0
    state = False
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == call[k]:
                check[i][j] = 1
                state = True
                break
        if state:
            break

    for i in range(5):
        if check[0][i] == 1:
            if i == 0:
                if down(0, i):
                    ans_count += 1
                if right_down(0, i):
                    ans_count += 1
                if right(0, i):
                    ans_count += 1
            elif i == 4:
                if left_down(0, i):
                    ans_count += 1
                if down(0, i):
                    ans_count += 1
            else:
                if down(0, i):
                    ans_count += 1

    for i in range(1, 5):
        if check[i][0] == 1 and right(i, 0):
            ans_count += 1

    if ans_count >= 3:
        print(k+1)
        sys.exit(0)