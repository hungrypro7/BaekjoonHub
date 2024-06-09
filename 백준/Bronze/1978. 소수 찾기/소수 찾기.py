n = int(input())
decimal = list(map(int, input().split()))
ans = 0
def prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
for i in decimal:
    if prime(i):
        ans += 1
print(ans)