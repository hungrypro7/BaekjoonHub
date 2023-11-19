n = int(input())
if n <= 2:
    print('1/', n, sep='')
for i in range(1, n):
    if n > i:
        n -= i
    else:
        if i % 2 == 0:
            print(n, '/', i+1-n, sep='')
            break
        else:
            print(i+1-n, '/', n, sep='')
            break