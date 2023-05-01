a = list(input())
b = list(input())
remove = len(a) + len(b)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a[i] = '0'
            b[j] = '1'
            remove -= 2

print(remove)