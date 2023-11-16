n = int(input())
square = [[0] * 100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x-1, x+9):
        for k in range(y-1, y+9):
            if square[j][k] != 1:
                square[j][k] = 1
ans = 0
for i in square:
    ans += sum(i)
print(ans)