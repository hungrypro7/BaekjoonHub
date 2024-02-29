import sys
input = sys.stdin.readline
n = int(input())
inq = []
for i in range(n):
  res, st, ba = map(int, input().split())
  inq.append((str(res), st, ba))

ans = []
for i in range(100, 1000):
    temp = str(i)
    if temp[0] != temp[1] and temp[1] != temp[2] and temp[0] != temp[2] and (temp[0] != '0' and temp[1] != '0' and temp[2] != '0'):
        for j in range(n):    # 질문 순회
            s, b = 0, 0
            for k in range(3):
                if inq[j][0][k] == temp[k]:
                    s += 1
                elif inq[j][0][k] in temp:
                    b += 1
            if s == inq[j][1] and b == inq[j][2]:
                if j == n-1:
                    ans.append(temp)
                continue
            else:
                break
print(len(ans))