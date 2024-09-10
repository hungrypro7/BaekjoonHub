h, w = map(int, input().split())    # 세로, 가로 길이
block_height = list(map(int, input().split()))    # 블록 높이를 입력 받음
block = [[0] * w for _ in range(h)]

for i in range(w):
    bh = block_height[i]
    for j in range(bh):
        block[j][i] = 1

water = 0    # 물의 총량
for i in range(h):
    start, end = 0, 0
    for k in range(w):
        if block[i][k] == 1:
            start = k    # 왼쪽
            break
    for k in range(w-1, -1, -1):
        if block[i][k] == 1:
            end = k    # 오른쪽
            break

    if start == end:
        continue

    for k in range(start, end):
        if block[i][k] == 0:
            water += 1

print(water)