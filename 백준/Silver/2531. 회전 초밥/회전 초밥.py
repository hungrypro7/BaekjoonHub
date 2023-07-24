n, d, k, c = map(int, input().split())      # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰번호
sushi = []
for i in range(n):
    num = int(input())
    sushi.append(num)
sushi = sushi + sushi[:k-1]
p = 0
sushi_set = set(sushi)
ans = len(sushi_set)
ans2 = 0
while p != n:
    once_pick = sushi[p:p+k]
    if ans >= len(sushi_set) - len(set(once_pick)):
        ans = len(sushi_set) - len(set(once_pick))
        ans2 = len(once_pick)
        ans3 = list(set(once_pick))
    p += 1

ans3.append(c)
print(len(set(ans3)))