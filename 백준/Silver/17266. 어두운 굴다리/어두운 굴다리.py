import sys
input = sys.stdin.readline
n = int(input())    # 굴다리의 개수
m = int(input())    # 가로등의 개수
position = list(map(int, input().split()))
ans = position[0]
for i in range(m-1):
    if (position[i+1] - position[i]) % 2 == 0:
        a = int((position[i+1] - position[i]) // 2)
    else:
        a = int((position[i+1] - position[i])/2) + 1
    ans = max(ans, a)
ans = max(n-position[-1], ans)
print(ans)