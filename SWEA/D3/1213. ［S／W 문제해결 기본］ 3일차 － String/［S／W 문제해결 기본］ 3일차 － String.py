test_case = 10
for i in range(1, test_case+1):
    t_num = int(input())    # 테스트 케이스 번호
    target = input()    # 찾을 문자열
    search = input()    # 검색할 문장
    ans = 0

    length1 = len(target)
    length2 = len(search)
    for j in range(length2):
        if search[j:j+length1] == target:
            ans += 1

    te = '#' + str(i)
    print(te, ans)