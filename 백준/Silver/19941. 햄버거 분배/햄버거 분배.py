n, k = map(int, input().split())
position = list(input())
result = 0
for i in range(n):
    if position[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j <= n-1 and position[j] == 'H':
                result += 1
                position[j] = 0
                break

print(result)