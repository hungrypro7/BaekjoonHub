import sys
input = sys.stdin.readline
n, l = map(int, input().split())    # 지도 크기, 경사로 크기
maps = []

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

for i in range(n):
    maps.append(list(map(int, input().split())))

cnt = 0
for i in range(n):    # 가로
    poss_pass = True    # 길 생성 여부
    check = [0] * n
    for j in range(n-1):

        if abs(maps[i][j] - maps[i][j+1]) > 1:    # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우 (2 이상인 경우)
            poss_pass = False
            break

        if maps[i][j] - maps[i][j+1] == 1:    # 왼쪽이 더 클 때
            if j+1+l > n:    # 경사로를 놓다가 범위를 벗어나는 경우
                poss_pass = False
            elif maps[i][j+1:j+1+l].count(maps[i][j+1]) != l:    # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                poss_pass = False
            elif 1 in check[j+1:j+1+l]:    # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                poss_pass = False
            else:
                for k in range(j+1, j+1+l):
                    check[k] = 1

        if maps[i][j+1] - maps[i][j] == 1:    # 오른쪽이 더 클 때
            if j+1-l < 0:    # 경사로를 놓다가 범위를 벗어나는 경우
                poss_pass = False
            elif maps[i][j+1-l:j+1].count(maps[i][j]) != l:    # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                poss_pass = False
            elif 1 in check[j+1-l:j+1]:    # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                poss_pass = False
            else:
                for k in range(j+1-l, j+1):
                    check[k] = 1

    if poss_pass:
        cnt += 1

maps = rotate_90(maps)
for i in range(n):    # 세로
    poss_pass = True    # 길 생성 여부
    check = [0] * n
    for j in range(n-1):

        if abs(maps[i][j] - maps[i][j+1]) > 1:    # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우 (2 이상인 경우)
            poss_pass = False
            break

        if maps[i][j] - maps[i][j+1] == 1:    # 왼쪽이 더 클 때
            if j+1+l > n:    # 경사로를 놓다가 범위를 벗어나는 경우
                poss_pass = False
            elif maps[i][j+1:j+1+l].count(maps[i][j+1]) != l:    # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                poss_pass = False
            elif 1 in check[j+1:j+1+l]:    # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                poss_pass = False
            else:
                for k in range(j+1, j+1+l):
                    check[k] = 1

        if maps[i][j+1] - maps[i][j] == 1:    # 오른쪽이 더 클 때
            if j+1-l < 0:    # 경사로를 놓다가 범위를 벗어나는 경우
                poss_pass = False
            elif maps[i][j+1-l:j+1].count(maps[i][j]) != l:    # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                poss_pass = False
            elif 1 in check[j+1-l:j+1]:    # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                poss_pass = False
            else:
                for k in range(j+1-l, j+1):
                    check[k] = 1

    if poss_pass:
        cnt += 1

print(cnt)