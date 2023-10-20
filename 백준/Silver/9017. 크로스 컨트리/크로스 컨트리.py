import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))      # 길이 : n
    count = {}
    for j in data:
        if j in count:
            count[j] += 1
        else:
            count[j] = 1

    dele = []
    for j in count.items():
        if j[1] < 6:
            dele.append(j[0])

    score = {}
    sc = 1
    for j in data:
        if j not in dele:
            if j in score:
                if score[j][0] < 4:
                    score[j][0] += 1
                    score[j][1] += sc
                elif score[j][0] == 4:
                    score[j][0] += 1
                    score[j][2] += sc
            else:
                score[j] = [1, sc, 0]    # 주자 수, 상위 4명 점수의 합, 5번째 점수
            sc += 1

    score = sorted(score.items(), key=lambda x:(x[1][1], x[1][2]))

    print(score[0][0])