import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
cc = list(map(int, input().split()))
cc.sort()
diff = []
for i in range(1, len(cc)):
    diff.append(cc[i]-cc[i-1])
diff.sort()
ans = 0
for i in range(n-k):
    ans += diff[i]
print(ans)