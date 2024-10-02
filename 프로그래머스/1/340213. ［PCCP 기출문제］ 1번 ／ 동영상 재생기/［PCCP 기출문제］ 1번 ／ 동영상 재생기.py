def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    pos_minute, pos_seconds = int(pos[:2]), int(pos[3:])
    for i in commands:    # commands 순회
        
        ost = 60 * int(op_start[:2]) + int(op_start[3:]) # 오프닝 시작 시간
        oet = 60 * int(op_end[:2]) + int(op_end[3:]) # 오프닝 종료 시간
        curt = 60 * int(pos_minute) + int(pos_seconds)    # 현재 시간
        end = 60 * int(video_len[:2]) + int(video_len[3:])
        
        if ost <= curt <= oet:    # 오프닝 종료 시간으로 이동
            pos_minute = int(op_end[:2])
            pos_seconds = int(op_end[3:])
        
        if i == "next":    # 10초 뒤로
            if end - curt < 10:
                pos_minute = int(video_len[:2])
                pos_seconds = int(video_len[3:])
            elif pos_seconds < 50:
                pos_seconds += 10
            else:
                pos_seconds = (pos_seconds + 10) % 60
                pos_minute += 1
        else:    # 10초 앞으로
            if pos_seconds < 10:
                if pos_minute == 0:
                    pos_minute, pos_seconds = 0, 0
                else:
                    pos_seconds = 60 - abs(pos_seconds - 10)
                    pos_minute -= 1
            else:
                pos_seconds -= 10
    
        curt = 60 * int(pos_minute) + int(pos_seconds)    # 현재 시간
        
        if ost <= curt <= oet:    # 오프닝 종료 시간으로 이동
            pos_minute = int(op_end[:2])
            pos_seconds = int(op_end[3:])
    
    if pos_minute < 10:
        answer += '0' + str(pos_minute)
    else:
        answer += str(pos_minute)
        
    answer += ':'

    if pos_seconds < 10:
        answer += '0' + str(pos_seconds)
    else:
        answer += str(pos_seconds)
        
    return answer