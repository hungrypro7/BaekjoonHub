N = int(input())
p = []
money = 0
for i in range(N):
    p.append(int(input()))
p.sort()
p.reverse()
for j in range(N):
    if p[j] - j < 0:
        continue
    money += p[j] - j

print(money)