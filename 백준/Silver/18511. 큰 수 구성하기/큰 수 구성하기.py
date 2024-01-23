import sys
input = sys.stdin.readline
n, k = map(int, input().split())
k_ele = list(map(int, input().split()))
ans = 0
state = False
for i in range(n, -1, -1):
    for idx, j in enumerate(str(i)):
        if int(j) not in k_ele:
            break
        elif idx == len(str(i))-1 and int(j) in k_ele:
            ans = i
            state = True
    if state:
        break
print(ans)