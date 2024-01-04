import sys
input = sys.stdin.readline
n = int(input())
A = []
B = []
move_to_a = []
move_to_b = []
for i in range(n-1):
    a, b, a_to_b, b_to_a = map(int, input().split())
    A.append(a)
    B.append(b)
    move_to_b.append(a_to_b)
    move_to_a.append(b_to_a)
a, b = map(int, input().split())
A.append(a)
B.append(b)
for i in range(1, n):
    A[i] = min(move_to_a[i-1]+B[i-1], A[i-1]) + A[i]
    B[i] = min(move_to_b[i-1]+A[i-1], B[i-1]) + B[i]
print(min(A[-1], B[-1]))