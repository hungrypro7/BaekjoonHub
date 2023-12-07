import math
n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    ans = 0
    for j in range(1, data[0]+1):
        for k in range(j+1, data[0]+1):
            ans += math.gcd(data[j], data[k])
    print(ans)