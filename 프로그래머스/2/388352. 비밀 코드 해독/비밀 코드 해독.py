from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    iter = [i for i in range(1, n+1)]
    
    for i in combinations(iter, 5):
        li = list(i)
        
        check = 0
        for idx, pwd in enumerate(q):
            
            co = 0
            for le in li:
                if le in pwd:
                    co += 1
                    
            if ans[idx] == co:
                check += 1
                continue
            else:
                break
        
        if check == len(ans):
            answer += 1
    
    return answer