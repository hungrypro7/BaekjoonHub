A, B = map(int, input().split())
count = 1
while(A != B):
    if (B < A):
        count = -1
        break
    c = str(B)
    if str(c[-1]) == '1':
        B = int(c[:-1])
        count += 1
    elif B % 2 == 0:
        B = B // 2
        count += 1
    else:
        count = -1
        break
print(count)