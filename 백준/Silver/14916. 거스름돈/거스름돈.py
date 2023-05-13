n = int(input())
count = 0
while(n):
    if n >= 10:
        count += 1
        n -= 5
    else:
        if n == 5 or n == 7 or n == 9:
            count += 1
            n -= 5
        elif n ==1 or n == 3:
            count = -1
            n = 0
        else:
            count += 1
            n -= 2

print(count)