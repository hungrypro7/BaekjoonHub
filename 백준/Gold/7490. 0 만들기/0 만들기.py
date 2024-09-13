def backtrack(n, cur, exp):
    if cur == n:
        ans = eval(exp.replace(' ', ''))
        if ans == 0:
            ans_list.append(exp)
        return
    else:
        backtrack(n, cur + 1, exp + ' ' + str(cur + 1))
        backtrack(n, cur + 1, exp + '+' + str(cur + 1))
        backtrack(n, cur + 1, exp + '-' + str(cur + 1))

num = int(input())    # 테스트 케이스 개수
for i in range(num):
    n = int(input())
    ans_list = []
    backtrack(n, 1, '1')
    for i in ans_list:
        print(i)
    print()