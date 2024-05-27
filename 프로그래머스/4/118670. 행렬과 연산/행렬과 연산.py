from collections import deque

def solution(rc, operations):
    r, c = len(rc), len(rc[0])
    l_col = deque([rc[i][0] for i in range(r)])
    r_col = deque([rc[i][c-1] for i in range(r)])
    rows = deque([deque(rc[i][1:c-1]) for i in range(r)])
    
    for i in operations:
        if i == "ShiftRow":
            l_col.appendleft(l_col.pop())
            rows.appendleft(rows.pop())
            r_col.appendleft(r_col.pop())
        else:
            rows[0].appendleft(l_col.popleft())
            r_col.appendleft(rows[0].pop())
            rows[r-1].append(r_col.pop())
            l_col.append(rows[r-1].popleft())
            
    answer = []
    for i in range(r):
        answer.append([l_col[i]] + list(rows[i]) + [r_col[i]])
    return answer