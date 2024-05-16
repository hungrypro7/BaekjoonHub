test_case = 10
for i in range(1, test_case+1):
    array = []
    a = int(input())
    for j in range(100):
        array.append(list(map(int, input().strip().split(' '))))

    ans = 0

    # 행의 합
    for j in range(100):
        ans = max(ans, sum(array[j]))

    # 열의 합
    for j in range(100):
        temp = 0
        for k in range(100):
            temp += array[k][j]
        ans = max(ans, temp)

    # 좌상 대각선 합
    temp = 0
    for j in range(100):
        temp += array[j][j]
    ans = max(ans, temp)

    # 우상 대각선 합합
    temp = 0
    for j in range(100):
        temp += array[j][99-j]
    ans = max(ans, temp)

    te = '#'+str(i)
    print(te, ans)