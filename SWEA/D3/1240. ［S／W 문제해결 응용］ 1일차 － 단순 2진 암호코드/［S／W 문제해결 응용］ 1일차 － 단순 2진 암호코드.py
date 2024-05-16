test_case = int(input())
for i in range(1, test_case+1):
    n, m = map(int, input().strip().split(' '))      # 세로, 가로 크기

    arr = []
    for j in range(n):
        arr.append(list(map(int, input().strip())))

    # 암호 코드 탐색
    ans = 0
    password = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
    new_pass = []       # 암호 저장
    state = False
    for j in range(n):
        for k in range(m-1, -1, -1):
            if arr[j][k] == 1:
                state = True
                temp = arr[j][k-55:k+1]
                break
        if state:
            break

    for j in range(8):
        new_pass.append(password[''.join(map(str, temp[7*j:7*(j+1)]))])

    # 올바른 암호코드인지 판별
    odd = new_pass[0] + new_pass[2] + new_pass[4] + new_pass[6]    # 홀수
    even = new_pass[1] + new_pass[3] + new_pass[5] + new_pass[7]    # 짝수

    if ((3 * odd) + even) % 10 == 0:
        ans = odd + even

    te = '#' + str(i)
    print(te, ans)