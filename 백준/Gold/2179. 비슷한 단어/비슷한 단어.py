import sys
input = sys.stdin.readline

def check(a, b):
    cnt = 0
    leng = min(len(a), len(b))
    for i in range(leng):
        if a[i] == b[i]: cnt += 1
        else: break
    return cnt

n = int(input())
word = []
for i in range(n):
    word.append([input().rstrip('\n'), i])
word2 = sorted(word)
length = [0] * (n+1)
max_leng = 0
for i in range(n-1):
    temp = check(word2[i][0], word2[i+1][0])

    max_leng = max(max_leng, temp)

    length[word2[i][1]] = max(length[word2[i][1]], temp)
    length[word2[i+1][1]] = max(length[word2[i+1][1]], temp)

count = 0
temp = ''
for j in range(n+1):
    if length[j] == max(length) and count == 0:
        print(word[j][0])
        count += 1
        temp = word[j][0][:max(length)]
    elif length[j] == max(length) and word[j][0][:max(length)] == temp:
        count += 1
        print(word[j][0])
    if count == 2:
        break