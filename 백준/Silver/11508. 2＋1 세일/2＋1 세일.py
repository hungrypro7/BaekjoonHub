N = int(input())
dairy_product = []
for i in range(N):
    dairy_product.append(int(input()))
money = 0
dairy_product.sort()

if N % 3 == 1:
    money += dairy_product[0]
    del dairy_product[0]
    N -= 1
elif N % 3 == 2:
    money += sum(dairy_product[0:2])
    del dairy_product[0:2]
    N -= 2

i = 0
while(N != 0):
    money += sum(dairy_product[i+1:i+3])
    i += 3
    N -= 3

print(money)