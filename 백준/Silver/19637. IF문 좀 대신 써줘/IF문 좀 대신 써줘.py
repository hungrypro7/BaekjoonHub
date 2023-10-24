import sys
input = sys.stdin.readline
n, m = map(int, input().split())
combat = []
for i in range(n):
    call, power = input().split()
    combat.append((call, int(power)))
combat.sort(key=lambda x: int(x[1]))
data = [int(input()) for _ in range(m)]
for j in data:
    right = len(combat)
    left = 0
    ans = 0
    while left <= right:
        mid = (left+right)//2
        if combat[mid][1] >= j:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(combat[ans][0])