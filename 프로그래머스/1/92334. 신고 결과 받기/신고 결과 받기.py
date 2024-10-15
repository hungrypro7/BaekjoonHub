def solution(id_list, report, k):
    answer = []
    
    answer = [0] * len(id_list)
    mem_counter = {}    # 신고당한 횟수 저장
    for i in id_list:
        mem_counter[i] = 0
    
    report = list(set(report))
    mem = {}
    for i in report:    # 신고한 사람, 신고당한 사람 저장
        caller, callee = i.split(' ')
        mem_counter[callee] += 1
    
    for i in report:    # 처리결과
        caller, callee = i.split(' ')
        if mem_counter[callee] >= k:
            answer[id_list.index(caller)] += 1
        
    return answer