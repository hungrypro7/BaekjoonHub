import sys
input = sys.stdin.readline
n = int(input())    # 시험장 개수
a = list(map(int, input().split()))    # 응시자 수
b, c = map(int, input().split())    # 총감독관, 부감독관
ans = 0
for i in range(n):
    if a[i] >= b:
        a[i] -= b
        ans += 1
        if a[i] % c > 0:
            ans += (a[i] // c) + 1
        else:
            ans += a[i] // c
    else:
        ans += 1
print(ans)