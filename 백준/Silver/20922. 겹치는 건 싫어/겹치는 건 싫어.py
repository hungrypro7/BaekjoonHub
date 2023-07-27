import sys
input = sys.stdin.readline
n, k = map(int, input().split())
an = list(map(int, input().split()))
left, right = 0, 0
state = [0] * (max(an)+1)
len = 0
while right <= n-1:
    if state[an[right]] >= k:
        state[an[left]] -= 1
        left += 1
    else:
        state[an[right]] += 1
        right += 1
    len = max(len, right-left)
print(len)