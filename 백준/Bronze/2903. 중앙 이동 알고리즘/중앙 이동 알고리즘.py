a = [3]
n = int(input())
i = 2
while len(a) != n:
    a.append(a[-1] + 2 ** (i-1))
    i += 1
print(a[-1] ** 2)