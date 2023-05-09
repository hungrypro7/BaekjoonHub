n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()
i, j = 0, n-1
count = 0
while(i < j):
    if numbers[i] + numbers[j] == x:
        count += 1
        i += 1
        j -= 1
    elif numbers[i] + numbers[j] > x:
        j -= 1
    else:
        i += 1
print(count)