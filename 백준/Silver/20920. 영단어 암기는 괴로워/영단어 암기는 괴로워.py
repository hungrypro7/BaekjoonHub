import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word = {}
for i in range(n):
    w = input().rstrip()
    if w in word:
        word[w] += 1
    else:
        if len(w) >= m:
            word[w] = 1
words = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in words:
    print(i[0])