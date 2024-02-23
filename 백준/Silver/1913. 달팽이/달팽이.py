import sys
n = int(input())
find_position = int(input())
mat = [[0] * n for _ in range(n)]
x, y = n // 2, n // 2
count = 1
mat[x][y] = count
for i in range(n//2):
    x -= 1
    for j in range((2*(i+1))-1):    # 가로 go right
        count += 1
        mat[x][y] = count
        y += 1
    count += 1
    mat[x][y] = count
    x += 1
    for j in range((2*(i+1))-1):    # 세로 go down
        count += 1
        mat[x][y] = count
        x += 1
    count += 1
    mat[x][y] = count
    y -= 1
    for j in range((2*(i+1))-1):    # 가로 go left
        count += 1
        mat[x][y] = count
        y -= 1
    count += 1
    mat[x][y] = count
    x -= 1
    for j in range((2*(i+1))-1):    # 세로 go up
        count += 1
        mat[x][y] = count
        x -= 1

    count += 1
    mat[x][y] = count

for i in mat:
    print(*i)

for i in range(n):
    for j in range(n):
        if mat[i][j] == find_position:
            print(i+1, j+1)
            sys.exit()