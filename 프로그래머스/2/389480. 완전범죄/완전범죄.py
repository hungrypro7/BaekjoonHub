import math

def solution(info, n, m):
    
    # 1. 초기 dp
    dp = [math.inf] * n
    dp[0] = 0
    
    # 2. 물건 하나씩 처리
    for a_cost, b_cost in info:
        next_dp = [math.inf] * n    # 물건마다 새 배열 생성
        
        # 3. 가능한 상태 순회
        for a in range(n):
            if dp[a] == math.inf:
                continue
        
            b = dp[a]    # A가 a개, B가 b개 가지고 있음
            
            # 4-1. A가 훔치는 경우 (새 A = a + a_cost, 새 B = b)
            if a + a_cost < n:
                next_dp[a + a_cost] = min(next_dp[a + a_cost], b)
            
            # 4-2. B가 훔지는 경우 (새 A = a, 새 B = b + b_cost)
            if b + b_cost < m:
                next_dp[a] = min(next_dp[a], b + b_cost)
        
        # 5. 갱신
        dp = next_dp
        
    # 6. 정담 찾기
    for a in range(n):
        if dp[a] < m:
            return a
    
    return -1
