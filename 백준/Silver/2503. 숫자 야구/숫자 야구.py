n = int(input())
record = []
for i in range(n):
    record.append(list(map(str, input().split())))

def three_differ(num):
    a = num[0]
    b = num[1]
    c = num[2]
    if a == '0' or b == '0' or c == '0':
        return False
    if a != b and b != c and a != c:
        return True
    return False

def dec_s_b(a, b):      # a는 비교하고자 하는 수, b는 123, 356, 327, 489
    strike, ball = 0, 0
    for i in range(3):      # 스트라이크 판별
        if a[i] == b[i]:
            strike += 1
        elif a[i] in b:
            ball += 1
    return [str(strike), str(ball)]

ans = 0
count = 0
for j in range(100, 999):
    if three_differ(str(j)):
        for k in range(n):
            if dec_s_b(str(j), record[k][0]) == record[k][1:3]:
                count += 1
        if count == n:
            ans += 1
        count = 0

print(ans)