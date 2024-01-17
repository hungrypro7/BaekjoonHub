import sys
input = sys.stdin.readline
a = int(input())        # 사람 수
t = int(input())        # 번째 T
bd = int(input())       # 뻔 = 0 / 데기 = 1

peo = [i for i in range(a)]
po = [-1, 0, -1]    # point, 번째, 뻔 / 데기

n = 1
while True:
    for i in range(2):
        po[0] += 1
        po[1] += 1
        po[2] = 0

        if po[1] == t and po[2] == bd:
            print(po[0] % a)
            sys.exit()

        po[0] += 1
        po[2] = 1

        if po[1] == t and po[2] == bd:
            print(po[0] % a)
            sys.exit()

    for i in range(n+1):
        po[0] += 1
        po[1] += 1
        po[2] = 0
        if po[1] == t and po[2] == bd:
            print(po[0] % a)
            sys.exit()

    po[1] -= n+1
    for i in range(n+1):
        po[0] += 1
        po[1] += 1
        po[2] = 1
        if po[1] == t and po[2] == bd:
            print(po[0] % a)
            sys.exit()

    n += 1