N = int(input())
t = list(map(int, input().split()))
t.sort()
max = 0
a = 0
while(t):
    if len(t) == 1:
        a = t[0]
        del t[0]
        break
    if len(t) % 2 == 1:
        a = t[0] + t[-2]
        del t[0]
        del t[-2]
    else:
        a = t[0] + t[-1]
        del t[0]
        del t[-1]
    if max < a:
        max = a

print(max)