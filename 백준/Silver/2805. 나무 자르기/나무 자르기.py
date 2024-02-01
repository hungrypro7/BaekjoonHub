import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # 나무의 수, 나무의 길이
tree_height = list(map(int, input().split()))
start, end = 1, max(tree_height)
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in tree_height:
        if i > mid:
            temp += i - mid
    if temp >= m:
        start = mid + 1
    elif temp < m:
        end = mid - 1
print(end)