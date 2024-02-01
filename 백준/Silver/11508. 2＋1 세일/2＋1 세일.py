n = int(input())
milk_and_yogurt = []
for i in range(n):
    milk_and_yogurt.append(int(input()))
milk_and_yogurt.sort()
count = 0
ans = 0
for i in range(n-1, -1, -1):
    count += 1
    ans += milk_and_yogurt[i]
    if count == 3:
        count = 0
        ans -= milk_and_yogurt[i]
print(ans)