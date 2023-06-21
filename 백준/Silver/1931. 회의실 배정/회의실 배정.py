N = int(input())
A = [[0] * 2 for _ in range(N)]
count = 0

for i in range(N):
    s, e = map(int, input().split())
    A[i][0] = e
    A[i][1] = s

A.sort()
end = 0

for j in range(N):
    if A[j][1] >= end:
        end = A[j][0]
        count += 1

print(count)