n = int(input())
def sum_num(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

for j in range(n):
    if j + sum_num(j) == n:
        print(j)
        break
    if j == n-1:
        print(0)