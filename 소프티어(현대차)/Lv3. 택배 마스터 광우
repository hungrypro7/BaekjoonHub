import sys
import itertools
input = sys.stdin.readline
n, m, k = map(int, input().split())    # 레일 개수, 택배 바구니 무게, 일의 시행 횟수
pack = list(map(int, input().split()))
p = list(itertools.permutations(pack, n))
ans = 1000000
for queue in p:
    temp_ans = 0
    po = 0
    que = list(queue)
    for i in range(k):
        temp = 0
        while temp <= m:
            a = que.pop(0)
            que.append(a)
            temp += a
            if temp + que[0] > m:
                break
        po += temp
    temp_ans += po
    ans = min(ans, temp_ans)
print(ans)
