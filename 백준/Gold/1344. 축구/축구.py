import math
a = int(input())
b = int(input())
prime = [2, 3, 5, 7, 11, 13, 17]
combi = [153, 816, 8568, 31824, 31824, 8568, 18]
ansa, ansb = 0, 0
for i in range(7):
    ansa += (math.pow(a/100, prime[i]))*(math.pow(1-a/100, 18-prime[i]))*combi[i]
for i in range(7):
    ansb += (math.pow(b/100, prime[i]))*(math.pow(1-b/100, 18-prime[i]))*combi[i]
print(ansa+ansb-ansa*ansb)