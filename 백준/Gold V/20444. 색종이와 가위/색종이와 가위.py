import sys
input = sys.stdin.readline
n, k = map(int, input().split())
row, col = 0, n//2+1     # 가로, 세로
while row != col:
    mid = (row + col) // 2
    if (mid+1) * (n-mid+1) > k:
        col = mid
    elif (mid+1) * (n-mid+1) < k:
        row = mid + 1
    else:
        print('YES')
        sys.exit()
print('NO')