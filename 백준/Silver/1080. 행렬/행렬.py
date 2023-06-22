n, m = map(int, input().split())
matrix1 = []
for i in range(n):
    row = list(map(int, input()))
    if ' ' in row:
        while ' ' in row:
            row.remove(' ')
    matrix1.append(row)

matrix2 = []
for j in range(n):
    row = list(map(int, input()))
    if ' ' in row:
        while ' ' in row:
            row.remove(' ')
    matrix2.append(row)

count = 0
def convert(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            matrix1[i][j] = 1 - matrix1[i][j]

for i in range(n-2):
    for j in range(m-2):
        if matrix1[i][j] != matrix2[i][j]:
            convert(i, j)
            count += 1

flag = 1

for i in range(n):
    for j in range(m):
        if matrix1[i][j] != matrix2[i][j]:
            flag = 0
if flag:
    print(count)
else:
    print(-1)