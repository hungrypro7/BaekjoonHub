test_case = 10
for i in range(1, test_case+1):
    n = int(input())    # 원본 암호문의 길이
    original_password = list(map(str, input().strip().split(' ')))    # 원본 암호문
    order_n = int(input())    # 명령어 개수
    order = list(map(str, input().strip().split(' ')))    # 명령어

    for idx, j in enumerate(order):
        if j == 'I':
            x = int(order[idx+1])
            y = int(order[idx+2])
            original_password = original_password[:x] + order[idx+3:idx+3+y] + original_password[x:]
        elif j == 'D':
            x = int(order[idx+1])
            y = int(order[idx+2])
            original_password = original_password[:x] + original_password[x+y:]

    te = '#' + str(i)
    print(te, *original_password[:10])