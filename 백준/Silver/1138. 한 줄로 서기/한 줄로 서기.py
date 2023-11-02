import sys
input = sys.stdin.readline
n = int(input())       # 사람의 수
record = [0] * n
pos = list(map(int, input().split()))
record[pos[0]] = 1
for i in range(1, n):
    count = 0
    for j in range(n):
        if count == pos[i] and record[j] == 0:
            record[j] = i+1
            break
        if record[j] == 0:
            count += 1
print(' '.join(map(str, record)))