def gcd(a, b):
    if b == 0:
        return a
    else:
        if a > b:
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))