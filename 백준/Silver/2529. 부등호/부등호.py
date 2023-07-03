k = int(input())
sign = list(input().split())
visited = [0] * 10      # 0~9까지를 위한 배열
answer = []

def check(a, b, op):
    if op == '<':
        if a > b: return False
    if op == '>':
        if a < b: return False
    return True

def bt(idx, num):
    if idx == k+1:
        answer.append(num)
        return

    for i in range(10):
        if visited[i]: continue

        if idx == 0 or check(num[idx-1], str(i), sign[idx-1]):
            visited[i] = 1
            bt(idx+1, num+str(i))
            visited[i] = 0

bt(0, '')
print(max(answer))
print(min(answer))