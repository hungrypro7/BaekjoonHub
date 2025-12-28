n = int(input())

cnt = 0
while n > 0:
    # 1. n이 5로 나눠질 경우
    if n % 5 == 0:
        cnt += n // 5
        break

    # 2. n이 3으로 나눠질 경우
    n -= 3

    # 3. n이 5와 3의 조합으로 나눠 담을 수 있는 경우
    if n == 1 or n == 2:
        cnt = -1
        break

    # 4. 5와 3으로 나눠지지 않는 경우


    cnt += 1

print(cnt)