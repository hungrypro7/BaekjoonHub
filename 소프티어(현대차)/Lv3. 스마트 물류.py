# 그리디 알고리즘
import sys
n, k = map(int, input().split())
li = list(input())
count = 0
for i in range(n):
    if li[i] == 'P':
        for j in range(max(0, i-k), min(i+k+1, n)):
            if li[j] == 'H':
                li[j] = 0
                count += 1
                break
print(count)