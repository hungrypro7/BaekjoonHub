import sys
input = sys.stdin.readline
n, s = map(int, input().split())
seq = list(map(int, input().split()))
left, right, temp = 0, 0, 0
ans = 10e6
state = False
while right <= n:
    if temp >= s:
        state = True
        ans = min(ans, right - left)
        temp -= seq[left]
        left += 1
    else:
        if right <= n-1:
            temp += seq[right]
        right += 1

if state:
    print(ans)
else:
    print(0)