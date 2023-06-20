N = int(input())
honeys = list(map(int, input().split()))
max_list = []

bee1 = 0        # 첫 번째 시나리오 b h b
bee2 = N-1
amount1 = 0
max1 = 0
for i in range(1, bee2):
    honey = i
    amount1 += sum(honeys[bee1+1:honey+1]) + sum(honeys[honey:bee2])
    if max1 < amount1:
        max1 = amount1
    amount1 = 0
max_list.append(max1)

bee1 = 0        # 두 번째 시나리오 b b h
honey = N-1
amount2 = 0
max2 = 0
for i in range(bee1+1, honey):
    bee2 = i
    amount2 += sum(honeys[bee1+1:bee2]) + 2 * sum(honeys[bee2+1:honey+1])
    if max2 < amount2:
        max2 = amount2
    amount2 = 0
max_list.append(max2)

bee2 = N-1      # 세 번째 시나리오 h b b
honey = 0
max3 = 0
amount3 = 0
for i in range(1, bee2):
    bee1 = i
    amount3 += 2 * sum(honeys[honey:bee1]) + sum(honeys[bee1+1:bee2])
    if max3 < amount3:
        max3 = amount3
    amount3 = 0
max_list.append(max3)

print(max(max_list))