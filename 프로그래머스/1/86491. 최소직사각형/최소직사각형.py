def solution(sizes):
    answer = 0
    width = 0
    remain = []
    for w, h in sizes:
        if w >= h:
            width = max(width, w)
            remain.append(h)
        else:
            width = max(width, h)
            remain.append(w)
    remain.sort()
    answer = width * remain[-1]
    return answer

