import sys
input = sys.stdin.readline
n = int(input())    # 스위치 개수
switch = list(map(int, input().split()))
m = int(input())    # 학생 수
stu = []
for i in range(m):
    gender, num = map(int, input().split())
    stu.append((gender, num))

for i, j in stu:
    if i == 1:  # 남학생일 때
        for k in range(j-1, n, j):
            switch[k] = (switch[k] + 1) % 2
    else:   # 여학생일 때
        j -= 1
        p = 0
        if j < n // 2:
            if j == 0:
                switch[0] = (switch[0] + 1) % 2
                continue
            for k in range(j-1, -1, -1):
                p += 1
                if switch[j-p] != switch[j+p]:
                    for q in range(j-p+1, j+p):
                        switch[q] = (switch[q] + 1) % 2
                    break
                elif k == 0:
                    p += 1
                    for q in range(j+p-1, j-p, -1):
                        switch[q] = (switch[q] + 1) % 2
                    break
        else:
            if j == n-1:
                switch[n-1] = (switch[n-1] + 1) % 2
                continue
            for k in range(j+1, n):
                p += 1
                if switch[j-p] != switch[j+p]:
                    for q in range(j+p-1, j-p, -1):
                        switch[q] = (switch[q] + 1) % 2
                    break
                elif k == n-1:
                    p += 1
                    for q in range(j+p-1, j-p, -1):
                        switch[q] = (switch[q] + 1) % 2
                    break

for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')