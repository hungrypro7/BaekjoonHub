T = int(input())
for i in range(T):
    a = input()
    word=[]
    for ch in a:
        if ch == '(':
            word.append(ch)
        elif ch == ')':
            if len(word) == 0:
                print('NO')
                break
            else:
                word.pop()
    else: # break 문이 수행되지 않았을 때
        if len(word) == 0:
            print('YES')
        else:
            print('NO')