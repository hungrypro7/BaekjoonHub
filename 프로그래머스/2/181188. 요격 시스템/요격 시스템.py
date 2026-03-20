def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    tar = -1
    for s, e in targets:
        if s >= tar:
            answer += 1
            tar = e
    
    return answer