n, m = map(int, input().split())
chess = []
temp = []
answer = []
for i in range(n):
    row = list(input())
    chess.append(row)

def compare1(list):     # WBWBWBWB      8x8
    count = 0
    for i in range(8):  # row
        for j in range(8):  # column
            if i % 2 == 0:
                if j % 2 == 0 and list[i][j] == 'W':
                    continue
                elif j % 2 == 1 and list[i][j] == 'B':
                    continue
                else:
                    count += 1
            elif i % 2 == 1:
                if j % 2 == 1 and list[i][j] == 'W':
                    continue
                elif j % 2 == 0 and list[i][j] == 'B':
                    continue
                else:
                    count += 1
    return count

def compare2(list):     # BWBWBWBW       8x8
    count = 0
    for i in range(8):  # row
        for j in range(8):  # column
            if i % 2 == 0:
                if j % 2 == 0 and list[i][j] == 'B':
                    continue
                elif j % 2 == 1 and list[i][j] == 'W':
                    continue
                else:
                    count += 1
            elif i % 2 == 1:
                if j % 2 == 1 and list[i][j] == 'B':
                    continue
                elif j % 2 == 0 and list[i][j] == 'W':
                    continue
                else:
                    count += 1
    return count

for i in range(n-7):
    for j in range(m-7):
        for k in range(i, i+8):
            temp.append(chess[k][j:j+8])
        a = min(compare1(temp), compare2(temp))
        answer.append(a)
        temp = []

print(min(answer))