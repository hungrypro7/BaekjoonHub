dir = ['N', 'E', 'S', 'W']
point = 0
for i in range(10):
    s = int(input())
    if s == 1:
        point = (point + 1) % 4
    elif s == 2:
        point = (point + 2) % 4
    elif s == 3:
        point = (point - 1) % 4

print(dir[point])