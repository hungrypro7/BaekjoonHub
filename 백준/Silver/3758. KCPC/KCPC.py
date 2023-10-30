import sys
input = sys.stdin.readline
t = int(input())    # 테스트 데이터 수
for p in range(t):
    n, k, t, m = map(int, input().split())      # 팀 개수, 문제 수, 당신 팀 ID, 로그 엔트리 개수
    data = [[po, 0, 0, 0, {}] for po in range(n+1)]     # 팀 ID, 총 점수, 마지막으로 등장한 번수, 제출 횟수, 각 문항당 최대 점수
    for q in range(m):
        i, j, s = map(int, input().split())     # 팀 ID, 문제 번호, 획득한 점수
        if j in data[i][4]:
            if s > data[i][4][j]:
                data[i][4][j] = s
        else:
            data[i][4][j] = s
        data[i][1] = sum(data[i][4].values())
        data[i][2] = q
        data[i][3] += 1
    data.sort(key=lambda x : (-x[1], x[3], x[2]))
    for idx, z in enumerate(data):
        if z[0] == t:
            print(idx+1)
            break