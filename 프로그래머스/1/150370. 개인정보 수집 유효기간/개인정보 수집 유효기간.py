from datetime import datetime
def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = int(today.split('.')[0]), int(today.split('.')[1]), int(today.split('.')[2])
    
    terms_dict = {}
    for i in terms:     # 유효기간 dict에 type, 기간 저장
        terms_dict[i[0]] = int(i[2:])
    
    count = 1
    for i in privacies:
        valid_date = i[-1]
        date = i[:-2]
        date_year, date_month, date_day = int(date.split('.')[0]), int(date.split('.')[1]), int(date.split('.')[2])
        
        diff = 0
        if today_year == date_year:
            diff += 28 - date_day
            diff += (today_month - date_month - 1) * 28
            diff += today_day
        else:
            diff += 28 - date_day
            diff += (12 - date_month - 1) * 28
            diff += (today_year - date_year - 1) * 12 * 28
            diff += 28 * today_month
            diff += today_day

        if diff >= 28 * terms_dict[valid_date]:
            answer.append(count)

        count += 1
            
    return answer