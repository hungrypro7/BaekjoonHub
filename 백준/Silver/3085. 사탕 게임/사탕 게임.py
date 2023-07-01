n = int(input())
candy = []
for i in range(n):
    candy.append(list(input()))

ans = []
def inspect(N, list):
    temp = []
    for i in range(N):                  # 행 검사
        saved = []
        p = 0
        for j in range(N-1):
            if list[i][j] == list[i][j+1]:
                p += 1
                if j == N-2:
                    saved.append(p+1)
            else:
                saved.append(p+1)
                p = 0
        temp.append(max(saved))

    for i in range(N):              # 열 검사
        saved = []
        p = 0
        for j in range(N-1):
            if list[j][i] == list[j+1][i]:
                p += 1
                if j == N-2:
                    saved.append(p+1)
            else:
                saved.append(p+1)
                p = 0
        temp.append(max(saved))

    return max(temp)

for i in range(n):          # 인접한 행 검사
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            ans.append(inspect(n, candy))
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        else:
            ans.append(inspect(n, candy))

for i in range(n):          # 인접한 열 검사
    for j in range(n-1):
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            ans.append(inspect(n, candy))
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
        else:
            ans.append(inspect(n, candy))

print(max(ans))