import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
ans = n*(n+1)//2
left, right, temp = 0, 0, 0
state = [0] * (max(seq)+1)
while right <= n-1:
    if state[seq[right]] < 1:
        state[seq[right]] += 1
        right += 1
    else:
        state[seq[left]] -= 1
        left += 1
        temp += (n-right)
print(ans - temp)