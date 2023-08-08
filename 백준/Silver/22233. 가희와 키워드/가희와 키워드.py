import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word = dict()
ans = []
cnt = 0
for i in range(n):
    word[input().rstrip('\n')] = 1
    cnt += 1
for j in range(m):
    keyword = list(input().rstrip('\n').split(','))
    for k in keyword:
        if word.get(k):
            cnt -= 1
            del word[k]
    print(cnt)