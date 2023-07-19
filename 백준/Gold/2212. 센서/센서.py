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
print(sum(diff[:n-k]))