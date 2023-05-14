n = int(input())
lope = []
for i in range(n):
    k = int(input())
    lope.append(k)

lope.sort()

max = 0
for i in lope:
    if i > max:
        max = i

for j in range(1, len(lope)+1):
    if (len(lope) - j + 1) * lope[j-1] > max:
        max = (len(lope) - j + 1) * lope[j-1]

print(max)