import sys
while True:
    temp, ans = 0, []
    n = int(input())
    if n == -1:
        sys.exit(0)
    for i in range(1, n):
        if n % i == 0:
            temp += i
            ans.append(str(i))
    if temp == n:
        print(n, '= ', end='')
        print(' + '.join(ans))
    else:
        print(n, 'is NOT perfect.')