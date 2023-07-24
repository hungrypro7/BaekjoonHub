import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())      # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰번호
sushi = []
for i in range(n):
    num = int(input())
    sushi.append(num)
sushi = sushi + sushi[:k-1]     # 원형 큐 만들어줌
p = 0
sushi_set = set(sushi)
ans_len = len(sushi_set)
ans = []
while p != n:
    once_pick = sushi[p:p+k]
    if ans_len >= len(sushi_set) - len(set(once_pick)):
        ans_len = len(sushi_set) - len(set(once_pick))
        ans = list(set(once_pick))
    p += 1
ans.append(c)
print(len(set(ans)))