piece = [1, 1, 2, 2, 2, 8]
inp = list(map(int, input().split()))
for i in range(6):
    if piece[i] == inp[i]:
        print(0, end=' ')
    else:
        print(piece[i] - inp[i], end=' ')