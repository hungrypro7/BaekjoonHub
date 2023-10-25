def solution(answers):
    answer = []
    solver1 = [1,2,3,4,5] * 2000
    solver2 = [2,1,2,3,2,4,2,5] * 1250
    solver3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    s = [0, 0, 0]
    for i, ans in enumerate(answers):
        if ans == solver1[i]:
            s[0] += 1
        if ans == solver2[i]:
            s[1] += 1
        if ans == solver3[i]:
            s[2] += 1
    temp = max(s)
    for i in range(3):
        if temp == s[i]:
            answer.append(i+1)
    return answer