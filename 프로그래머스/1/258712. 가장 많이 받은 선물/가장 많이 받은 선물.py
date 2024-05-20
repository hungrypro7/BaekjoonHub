def solution(friends, gifts):
    answer = 0
    n = len(friends)
    table = [[0] * n for _ in range(n)]    # 선물지수 표
    
    for i in gifts:
        sender, receiver = i.split(' ')
        index1 = friends.index(sender)
        index2 = friends.index(receiver)
        table[index1][index2] += 1
    
    send_gift = [0] * n
    receive_gift = [0] * n
    for i in range(n):
        send_gift[i] = sum(table[i])    # 준 선물
    
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += table[j][i]
        receive_gift[i] = temp    # 받은 선물
    
    gift = [0] * n    # 선물 지수
    for i in range(n):
        gift[i] = send_gift[i] - receive_gift[i]
    
    total = [0] * n    # 전체 계산
    for i in range(n):
        for j in range(n):
            if table[i][j] > 0:   # 두 사람이 선물을 주고 받은 기록이 있다면
                if table[i][j] > table[j][i]:
                    total[i] += 1
                elif table[i][j] < table[j][i]:
                    total[j] += 1
                else:
                    if gift[i] > gift[j]:
                        total[i] += 1
                    elif gift[i] < gift[j]:
                        total[j] += 1
                table[i][j], table[j][i] = -1, -1
            elif table[i][j] == 0 and table[j][i] == 0:    # 두 사람이 선물을 주고 받은 기록이 하나도 없다면
                if gift[i] > gift[j]:
                    total[i] += 1
                elif gift[i] < gift[j]:
                    total[j] += 1
                table[i][j], table[j][i] = -1, -1

    answer = max(total)
    return answer