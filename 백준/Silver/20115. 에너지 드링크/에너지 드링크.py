N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
result = drinks[N-1]
for i in range(N-1):
    result += drinks[i]/2

if result % 1 == 0:
    print(int(result))
else:
    print(result)