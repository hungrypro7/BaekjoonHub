n = int(input())
rgb = []
for i in range(n):
    red, green, blue = map(int, input().split())
    rgb.append([red, green, blue])
for j in range(1, n):
    rgb[j][0] = min(rgb[j-1][1], rgb[j-1][2]) + rgb[j][0]
    rgb[j][1] = min(rgb[j-1][0], rgb[j-1][2]) + rgb[j][1]
    rgb[j][2] = min(rgb[j-1][0], rgb[j-1][1]) + rgb[j][2]
print(min(rgb[-1]))