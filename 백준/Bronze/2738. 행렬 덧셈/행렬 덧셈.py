import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2*n)]
ans = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(matrix[i][j]+matrix[i+n][j])
    ans.append(temp)
for i in ans:
    print(*i)