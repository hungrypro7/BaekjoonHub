import sys
board = list(input().split('.'))
ans = ''
for idx, i in enumerate(board):
    if len(i) == 0:
        ans += '.'
        continue
    elif len(i) % 2 == 1:
        print(-1)
        sys.exit(0)
    else:
        p = 0
        while p < len(i):
            if len(i) - p >= 4:
                ans += 'AAAA'
                p += 4
            elif len(i) - p >= 2:
                ans += 'BB'
                p += 2
    if idx != len(board) - 1:
        ans += '.'
if board[-1] == '':
    ans = ans[:-1]
print(ans)