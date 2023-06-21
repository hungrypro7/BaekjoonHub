N = int(input())
balls = input()
R, B = 0, 0
answer = []
for i in balls:
    if i == 'R':
        R += 1
    else:
        B += 1

r1, b1 = 0, 0
start, end = balls[0], balls[N-1]
for i in range(N):
    if balls[i] != balls[i-1] and i > 0:
        if balls[i-1] == 'R':
            r1 = i
        else:
            b1 = i
        break

r2, b2 = 0, 0
for j in range(N-2, -1, -1):
    if balls[j] != balls[j+1] and j < N-1:
        if balls[j+1] == 'R':
            r2 = N - 1 - j
        else:
            b2 = N - 1 - j
        break

answer.append(R-r1)
answer.append(R-r2)
answer.append(B-b1)
answer.append(B-b2)

print(min(answer))