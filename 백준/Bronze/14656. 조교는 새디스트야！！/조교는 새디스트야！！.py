n = int(input())
stu = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    if stu[i-1] != i:
        count += 1
print(count)