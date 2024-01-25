import sys
input = sys.stdin.readline
n = int(input())    # 스타박스 앞에 서 있는 사람의 수
tip = []
for i in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)
ans = 0
for i in range(n):
    if tip[i] - i >= 0:
        ans += tip[i] - i
print(ans)