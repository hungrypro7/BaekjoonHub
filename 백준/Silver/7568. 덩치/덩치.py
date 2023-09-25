n = int(input())
data = []
result = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

for i in range(n):
    a, b = data[i]
    temp = 1
    for j in range(n):
        if i == j:
            continue
        c, d = data[j]
        if a < c and b < d:
            temp += 1
    result[i] = temp

print(' '.join(map(str, result)))