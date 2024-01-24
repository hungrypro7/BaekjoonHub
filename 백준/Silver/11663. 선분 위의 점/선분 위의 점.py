import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dot = list(map(int, input().split()))
line = []
for i in range(m):
    s, e = map(int, input().split())
    line.append([s, e])
dot = sorted(dot)
def binary_search(start, end, target):
    mid = (start+end) // 2

    if start > end:
        return start - 1

    if dot[mid] > target:
        return binary_search(start, mid-1, target)
    elif dot[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return mid

for i in line:
    ans = 0
    a = binary_search(0, n-1, i[0])
    b = binary_search(0, n-1, i[1])
    if dot[a] == i[0]:
        ans += 1
    ans += abs(b - a)
    print(ans)
