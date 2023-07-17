s = int(input())
count = 0
num = 0
for i in range(1, s):
    if s - num < i or s == num:
        break
    num += i
    count += 1
if s == 1:
    count = 1
print(count)