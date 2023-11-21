a, b, c = map(int, input().split())
num = []
num.append(a)
num.append(b)
num.append(c)
num.sort()
temp = num[0] + num[1]
if num[2] >= num[0]+num[1]:
    print(temp+temp-1)
else:
    print(temp+num[2])