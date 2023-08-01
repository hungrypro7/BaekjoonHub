n = int(input())
words = []
for i in range(n):
    if i == 0:
        stan = str(input())
    else:
        word = str(input())
        words.append(word)
count = 0
for i in words:
    if len(i) == len(stan):     # 문자열 길이가 같을 때
        e = sorted(stan)
        f = sorted(i)
        if e == f:     # 순서만 바꿔놓은 경우
            count += 1
        else:       # 문자 하나를 바꿔놓은 경우
            for j in range(len(e)):
                if e[j] in f:
                    f.remove(e[j])
            if len(f) == 1:
                count += 1
    elif len(i)-len(stan) == 1:    # 문자를 하나 더 추가한 경우
        a = sorted(i)
        b = sorted(stan)
        a = ''.join(str(_) for _ in a)
        b = ''.join(str(_) for _ in b)
        state = False
        for j in range(len(a)):
            if a[:j] + a[j+1:] == b:
                state = True
        if state:
            count += 1
    elif len(stan)-len(i) == 1:     # 문자를 하나 제거한 경우
        c = sorted(i)
        d = sorted(stan)
        c = ''.join(str(_) for _ in c)
        d = ''.join(str(_) for _ in d)
        state = False
        for j in range(len(d)):
            if d[:j] + d[j+1:] == c:
                state = True
        if state:
            count += 1
print(count)