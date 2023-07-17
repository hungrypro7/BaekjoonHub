t = int(input())
count1, count2, count3 = 0, 0, 0
state = False
while t != 0:
    if t >= 300:
        t -= 300
        count1 += 1
    elif t >= 60:
        t -= 60
        count2 += 1
    elif t >= 10:
        t -= 10
        count3 += 1
    else:
        state = True
        break
if state:
    print(-1)
else:
    print(count1, count2, count3)