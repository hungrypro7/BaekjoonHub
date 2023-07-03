n = int(input())
def sum_num(n):
    sum_num = sum(map(int, str(n)))
    return sum_num

for j in range(n):
    if j + sum_num(j) == n:
        print(j)
        break
    if j == n-1:
        print(0)