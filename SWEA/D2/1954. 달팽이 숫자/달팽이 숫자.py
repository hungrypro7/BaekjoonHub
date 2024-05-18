t = int(input())
for i in range(1, t+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    count = 1
    p = 0
    while True:
        for j in range(p, n-p):    # ->
            snail[p][j] = count
            count += 1

        if n % 2 == 1 and count >= n*n:
            break

        for j in range(p+1, n-p-1):    # 아래
            snail[j][n-p-1] = count
            count += 1

        for j in range(n-p-1, p-1, -1):    # <-
            snail[n-p-1][j] = count
            count += 1

        for j in range(n-p-2, p, -1):    # 상
            snail[j][p] = count
            count += 1

        p += 1
        if n % 2 == 0 and count >= n*n:
            break

    te = '#' + str(i)
    print(te)
    for j in snail:
        print(*j)