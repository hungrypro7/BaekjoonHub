N, K = map(int, input().split())
man = [0] * 7
woman = [0] * 7
room = 0
for i in range(N):
    S, Y = map(int, input().split())
    if S == 1:  # 남학생인 경우
        man[Y] += 1
    else:   # 여학생인 경우
        woman[Y] += 1

for i in man:
    if i > 0 and i <= K:
        room += 1
    elif i > K:
        room += i // K
        room += 1

for i in woman:
    if i > 0 and i <= K:
        room += 1
    elif i > K:
        room += i // K
        room += 1

print(room)