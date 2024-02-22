keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
sl, sr = input().split()    # 현재 왼손, 오른손 위치
st = input()    # 문자열
for i in range(3):
    if sl in keyboard[i]:
        left = (i, keyboard[i].index(sl))
    if sr in keyboard[i]:
        right = (i, keyboard[i].index(sr))
time = 0
for i in st:    # 문자열을 하나씩 돌면서 탐색
    time += 1
    for j in range(3):
        if i in keyboard[j]:
            if (j == 0 and 0 <= keyboard[j].index(i) <= 4) or (j == 1 and 0 <= keyboard[j].index(i) <= 4) or (j == 2 and 0 <= keyboard[j].index(i) <= 3):
                x = (j, keyboard[j].index(i))
                time += abs(left[0]-x[0]) + abs(left[1]-x[1])
                left = (j, keyboard[j].index(i))
            else:
                y = (j, keyboard[j].index(i))
                time += abs(right[0]-y[0]) + abs(right[1]-y[1])
                right = (j, keyboard[j].index(i))
print(time)