import sys
import math
input = sys.stdin.readline
n = int(input())
a = math.isqrt(n)
if a ** 2 != n:
    print(a+1)
else:
    print(a)