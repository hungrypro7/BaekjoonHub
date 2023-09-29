import sys
input = sys.stdin.readline
while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        sys.exit(0)

    temp = max(a, b, c)

    if temp >= (a + b + c - temp):
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a != b and b != c and a != c:
            print('Scalene')
        else:
            print('Isosceles')
