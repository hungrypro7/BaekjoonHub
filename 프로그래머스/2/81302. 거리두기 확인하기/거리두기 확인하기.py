def solution(places):
    answer = []

    for room in places:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        dx2 = [-1, -1, 1, 1]
        dy2 = [-1, 1, -1, 1]
        
        state = 0
        for i in range(5):  # 회의실 탐색
            for j in range(5):
                if room[i][j] == 'P':  # 사람이 있을 때
                    for k in range(4):
                        # 맨해튼 거리 1에 사람 있을 때
                        nx1 = i + dx[k]
                        ny1 = j + dy[k]
                        if 0 <= nx1 < 5 and 0 <= ny1 < 5 and room[nx1][ny1] == 'P':
                            state = 1
                            break

                        # 맨해튼 거리 2에 사람 있을 때 (상하좌우)
                        nx2 = i + (2 * dx[k])
                        ny2 = j + (2 * dy[k])
                        # 중간에 테이블이 있으면
                        if 0 <= nx2 < 5 and 0 <= ny2 < 5 and room[nx2][ny2] == 'P' and room[nx1][ny1] != 'X':
                            state = 1
                            break

                        # 맨해튼 거리 2에 사람 있을 때 (상하좌우 대각선)
                        nx3 = i + dx2[k]
                        ny3 = j + dy2[k]
                        if 0 <= nx3 < 5 and 0 <= ny3 < 5 and room[nx3][ny3] == 'P':
                            if room[nx3][j] != 'X' or room[i][ny3] != 'X':
                                state = 1
                                break
                if state:
                    break
            if state:
                break
        if state:
            answer.append(0)
            continue
            
        answer.append(1)  # 올바르게 지키고 있으면 1 추가

    return answer