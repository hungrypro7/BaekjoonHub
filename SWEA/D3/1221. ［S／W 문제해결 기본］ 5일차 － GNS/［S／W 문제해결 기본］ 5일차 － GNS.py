t = int(input())
for i in range(1, t+1):
    te, l = map(str, input().strip().split(" "))
    num_list = list(map(str, input().strip().split(" ")))
    length = int(l)

    check_list = {'ZRO' : 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0}
    for j in range(length):
        check_list[num_list[j]] += 1

    print(te)
    for j in check_list.keys():
        for k in range(check_list[j]):
            print(j, end=' ')