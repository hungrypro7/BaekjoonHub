n = int(input())
mountain = list(map(int, input().split()))
ans = 0
height = mountain[0]
count = 0
for i in range(1, n):
    if mountain[i] > height:
        height = mountain[i]
        count = 0
    else:
        count += 1
    ans = max(count, ans)
print(ans)