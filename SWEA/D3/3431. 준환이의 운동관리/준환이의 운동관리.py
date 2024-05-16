t = int(input())
for i in range(1, t+1):
    l, u, x = list(map(int, input().strip().split(" ")))
    minute = 0

    if l <= x <= u:
        minute = 0
    elif x < l:
        minute = l - x
    elif x > u:
        minute = -1

    ans = '#' + str(i)
    print(ans, minute)