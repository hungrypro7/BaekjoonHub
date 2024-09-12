import math
n = int(input())    # 전체 용액의 수
sol = list(map(int, input().split()))    # 용액의 특성값
p, q = 0, n-1
ans = [0, 0]
temp = math.inf

while p < q:
    two_sum = sol[p] + sol[q]
    if two_sum > 0:
        if abs(two_sum) < temp:
            temp = abs(two_sum)
            ans[0], ans[1] = p, q
        q -= 1
    elif two_sum < 0:
        if abs(two_sum) < temp:
            temp = abs(two_sum)
            ans[0], ans[1] = p, q
        p += 1
    else:
        ans[0], ans[1] = p, q
        break

front, end = ans[0], ans[1]
print(sol[front], sol[end])
