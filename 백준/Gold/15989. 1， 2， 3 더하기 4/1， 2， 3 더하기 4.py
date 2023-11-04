import sys
input = sys.stdin.readline
t = int(input())    # 테스트 케이스 개수
record = [0, 1, 2, 3]
for i in range(t):
    n = int(input())
    if len(record) <= n:
        for j in range(len(record), n+1):
            record.append(1+(j//2)+record[j-3])
    print(record[n])