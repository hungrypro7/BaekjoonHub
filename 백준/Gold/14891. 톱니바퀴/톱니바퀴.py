import sys
gear = []
for i in range(4):      # 톱니바퀴의 상태
    gear.append(list(map(int, input())))

rotate = []
k = int(input())
for i in range(k):
    num, dir = map(int, input().split())    # 톱니바퀴 번호, 방향
    rotate.append((num, dir))

state = [0, 0, 0, 0, 0, 0, 0, 0]      # 1 (1, 2), (2, 3), (3, 4) 4
for i in range(k):
    state[1], state[2] = gear[0][2], gear[1][6]   # 맞물려 있는 상태를 갱신해 줌
    state[3], state[4] = gear[1][2], gear[2][6]
    state[5], state[6] = gear[2][2], gear[3][6]
    n, d = rotate[i][0], rotate[i][1]    # 돌릴 톱니 번호, 방향

    for j in range(n-2, -1, -1):
        if state[j*2+1] != state[j*2+2]:
            if abs(n-1-j) % 2 == 1:   # 홀수일 때 d 방향 반대
                if d == 1:
                    temp = gear[j][1:] + [gear[j][0]]
                else:
                    temp = [gear[j][-1]] + gear[j][:7]
            else:       # 짝수일 때 d 방향 동일
                if d == 1:
                    temp = [gear[j][-1]] + gear[j][:7]
                else:
                    temp = gear[j][1:] + [gear[j][0]]
            gear[j] = temp
        else:
            break

    for j in range(n, 4):
        if state[j*2] != state[j*2-1]:
            if abs(j-(n-1)) % 2 == 1:   # 홀수일 때 d 방향 반대
                if d == 1:
                    temp = gear[j][1:] + [gear[j][0]]
                else:
                    temp = [gear[j][-1]] + gear[j][:7]
            else:       # 짝수일 때 d 방향 동일
                if d == 1:
                    temp = [gear[j][-1]] + gear[j][:7]
                else:
                    temp = gear[j][1:] + [gear[j][0]]
            gear[j] = temp
        else:
            break

    # 맨 마지막에 n번 톱니 바퀴 회전
    if d == 1:     # 시계 방향
        temp = [gear[n-1][-1]] + gear[n-1][:7]
    else:   # 반시계 방향
        temp = gear[n-1][1:] + [gear[n-1][0]]
    gear[n-1] = temp

# 점수 계산
ans = 0
for i in range(4):
    if i == 0 and gear[i][0] == 1:
        ans += 1
    elif i == 1 and gear[i][0] == 1:
        ans += 2
    elif i == 2 and gear[i][0] == 1:
        ans += 4
    elif i == 3 and gear[i][0] == 1:
        ans += 8
print(ans)