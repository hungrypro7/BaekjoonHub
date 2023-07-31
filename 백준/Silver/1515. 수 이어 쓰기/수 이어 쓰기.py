import sys
input = sys.stdin.readline
num = input()
p, i = 0, 1
while p != len(num)-1:
    for j in str(i):
        if j == num[p]:
            p += 1
        if p == len(num)-1:
            print(str(i))
            break
    i += 1