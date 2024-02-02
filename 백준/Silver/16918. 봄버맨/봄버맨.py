r, c, n = map(int, input().split())     # 행, 열, 시간 (초)
matrix = []
for i in range(r):
    matrix.append(list(input()))

if n % 2 == 0:  # n이 짝수일 때는 모든 칸에 폭탄이 다 설치되어 있음
    for i in range(r):
        print('O' * c, end='')
        print()
else:
    # 1, 5, 9 ... 는 처음과 똑같이 출력
    if n == 1:
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end='')
            print()
    elif n % 4 == 1:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        ans = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 'O':
                    ans[i][j] = '.'
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            ans[nx][ny] = '.'

        ans2 = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if ans[i][j] == 'O':
                    ans2[i][j] = '.'
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            ans2[nx][ny] = '.'

        for i in range(r):
            for j in range(c):
                print(ans2[i][j], end='')
            print()

    # 3, 7, 11 ... 는 폭탄이 터지지 않은 부분 출력
    elif n % 4 == 3:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        ans = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 'O':
                    ans[i][j] = '.'
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            ans[nx][ny] = '.'

        for i in range(r):
            for j in range(c):
                print(ans[i][j], end='')
            print()