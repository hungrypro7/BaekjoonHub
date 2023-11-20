import sys
m = int(input())
n = int(input())
su = 0
min_num = 100000
def is_prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
for i in range(m, n+1):
    if is_prime(i):
        su += i
        if min_num >= i:
            min_num = i
if su == 0 and min_num == 100000:
    print(-1)
else:
    print(su)
    print(min_num)