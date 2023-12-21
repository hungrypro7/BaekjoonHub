import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
def two_count(a):
    if a < 2:
        return 0
    cnt = 0
    while a >= 2:
        cnt += a // 2
        a //= 2
    return cnt

def five_count(a):
    if a < 5:
        return 0
    cnt = 0
    while a >= 5:
        cnt += a // 5
        a //= 5
    return cnt

five_count = five_count(n) - five_count(n-m) - five_count(m)
two_count = two_count(n) - two_count(n-m) - two_count(m)
print(min(five_count, two_count))