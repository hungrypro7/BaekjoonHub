n = int(input())
sang = list(map(int, input().split()))
dic = {}
m = int(input())
num_card = list(map(int, input().split()))
for i in num_card:
    if i not in dic:
        dic[i] = 0
for j in sang:
    if j in dic:
        dic[j] += 1
print(*list(dic.values()))