t = int(input())
for i in range(t):
    word = dict()
    w = input()
    k = int(input())
    for j in range(len(w)):
        if w[j] in word:
            word[w[j]].append(j)
        else:
            word[w[j]] = [j]

    ans1 = 10000
    ans2 = 0
    state = True
    for j in word:
        temp = word.get(j)
        if len(temp) >= k:
            state = False
            for p in range(len(temp)-(k-1)):
                ans1 = min(ans1, temp[p+(k-1)]-temp[p]+1)
                ans2 = max(ans2, temp[p+(k-1)]-temp[p]+1)
    if state:
        print(-1)
        continue

    print(ans1, ans2)
