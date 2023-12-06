import math
m, n = map(int, input().split())
A = [0] * (n+1)

for i in range(2, n+1):
    A[i] = i

for j in range(2, int(math.sqrt(n)) + 1):
    if A[j] == 0:
        continue
    for k in range(j+j, n+1, j):
        A[k] = 0

for k in range(m, n+1):
    if A[k] != 0:
        print(A[k])