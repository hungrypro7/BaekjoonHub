from datetime import datetime, timedelta
import math

def time_diff(start, end):
    time1 = datetime.strptime(start, "%H:%M").time()
    time2 = datetime.strptime(end, "%H:%M").time()
    datetime1 = datetime.combine(datetime.today(), time1)
    datetime2 = datetime.combine(datetime.today(), time2)
    time_diff = datetime2 - datetime1
    during_time = int(time_diff.total_seconds() / 60)
    return during_time

def solution(fees, records):
    answer = []
    
    basic_time, basic_cost, unit_time, unit_cost = fees
    
    info = {}
    for i in records:
        time, car_num, ioo = i.split(' ')
        if ioo == "IN" and car_num not in info:    # 입차 시 차량 번호판, 시간 저장
            info[car_num] = [0, time, ioo]    # 요금, 시간, IN 저장
        elif ioo == "IN" and car_num in info:
            info[car_num][1] = time
            info[car_num][2] = ioo
        else:    # 출차 시 요금 계산해서 저장
            park_time = time_diff(info[car_num][1], time)
            info[car_num][0] += park_time
            info[car_num][1], info[car_num][2] = time, ioo
    
    for key, value in info.items():
        if value[2] == "IN":
            park_time = time_diff(value[1], "23:59")
            value[0] += park_time
    
    sort_num = sorted(info)
    
    for i in sort_num:
        if info[i][0] >= basic_time:
            cost = int(math.ceil((info[i][0] - basic_time) / unit_time) * unit_cost) + basic_cost
            answer.append(cost)
        else: 
            answer.append(basic_cost)
            
    return answer