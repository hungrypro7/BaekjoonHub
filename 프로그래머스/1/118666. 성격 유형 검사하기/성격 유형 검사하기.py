def solution(survey, choices):
    answer = ''
    personality = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for idx, j in enumerate(survey):
        choice = choices[idx]
        if choice == 1:
            score = j[0]
            personality[score] += 3
        elif choice == 2:
            score = j[0]
            personality[score] += 2
        elif choice == 3:
            score = j[0]
            personality[score] += 1
        elif choice == 5:
            score = j[1]
            personality[score] += 1
        elif choice == 6:
            score = j[1]
            personality[score] += 2
        elif choice == 7:
            score = j[1]
            personality[score] += 3
    print(personality)
    estimate = list(personality.keys())
    for idx, j in enumerate(estimate):
        if idx % 2 == 0:
            if personality[estimate[idx]] >= personality[estimate[idx+1]]:
                answer += estimate[idx]
            elif personality[estimate[idx]] < personality[estimate[idx+1]]:
                answer += estimate[idx+1]
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)