t = int(input())
for i in range(1, t+1):
    n, m, k = map(int, input().split())
    when_come = list(map(int, input().strip().split(' ')))    # 오는 사람들 시간
    time_table = [0] * 11112
    for j in when_come:
        time_table[j] += 1
    state = True

    time = 0    # 현재 시간
    count = 0    # 붕어빵 개수
    peo = 0    # 사람 수
    while True:
        if time > 0 and time % m == 0:
            count += k

        if time_table[time] > 0:
            if count >= time_table[time]:
                count -= time_table[time]
                peo += time_table[time]
            else:
                state = False
                break

        if peo == n:
            break

        time += 1

    te = '#' + str(i)
    print(te, end=' ')
    if state:
        print('Possible')
    else:
        print('Impossible')