import sys
N = int(sys.stdin.readline())
honeys = list(map(int, sys.stdin.readline().split()))
max_list = []
honeys_sigma = [0]
for i in range(N):
    honeys_sigma.append(honeys_sigma[i] + honeys[i])
honeys_sigma.remove(0)

bee1 = 0        # 첫 번째 시나리오 b h b
bee2 = N-1
amount1 = 0
max1 = 0
for i in range(1, bee2):
    honey = i
    amount1 += (honeys_sigma[honey] - honeys_sigma[bee1]) + (honeys_sigma[bee2-1] - honeys_sigma[honey] + honeys[honey])
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
    amount2 += (honeys_sigma[honey] - honeys_sigma[bee1] - honeys[bee2]) + (honeys_sigma[honey] - honeys_sigma[bee2])
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
    amount3 += honeys_sigma[bee1-1] + (honeys_sigma[bee2-1] - honeys[bee1])
    if max3 < amount3:
        max3 = amount3
    amount3 = 0
max_list.append(max3)

print(max(max_list))