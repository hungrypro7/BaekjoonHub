n = input()
thr = 0
for i in n:
    thr += int(i)
if thr % 3 == 0:
    a = sorted(n, reverse=True)
    temp = ''
    for i in a:
        temp += i
    if int(temp) % 30 == 0:
        ans = int(temp)
    else:
        ans = -1
else:
    ans = -1
print(ans)