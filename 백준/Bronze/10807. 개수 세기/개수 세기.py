n = int(input())
a = list(map(int, input().split()))
v = int(input())
sum = 0
for i in a:
    if i == v:
        sum += 1
print(sum)