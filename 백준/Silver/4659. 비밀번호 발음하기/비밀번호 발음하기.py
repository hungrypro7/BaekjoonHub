import sys
while True:
    testcase = input()
    if testcase == 'end':
        sys.exit(0)
    state = False
    if ('a' in testcase) or ('e' in testcase) or ('i' in testcase) or ('o' in testcase) or ('u' in testcase):
        if len(testcase) >= 3:
            for i in range(len(testcase)-2):
                con, ga = 0, 0      # 자음, 모음
                for j in testcase[i:i+3]:
                    if ord(j) == 97 or ord(j) == 101 or ord(j) == 105 or ord(j) == 111 or ord(j) == 117:
                        ga += 1
                    else:
                        con += 1
                if ga == 3 or con == 3:
                    state = False
                    break
                else:
                    state = True
        else:
            state = True

        if state:
            for k in range(len(testcase)-1):
                if testcase[k] == testcase[k+1]:
                    if (testcase[k:k+2] == 'ee') or (testcase[k:k+2] == 'oo'):
                        state = True
                    else:
                        state = False
    if state:
        print('<', testcase, '>', sep='', end=' ')
        print('is acceptable.')
    else:
        print('<', testcase, '>', sep='', end=' ')
        print('is not acceptable.')
