n = int(input())
ans = []
for i in range(n):
    con = input()
    j = 0
    temp = ''
    for j in range(len(con)):
        if ord(con[j]) >= 48 and ord(con[j]) <= 57:
            temp += con[j]
            if j == len(con)-1:
                ans.append(int(temp))
        elif (ord(con[j]) >= 97 and ord(con[j]) <= 122):
            if len(temp) >= 1:
                ans.append(int(temp))
                temp = ''
ans.sort()
for i in ans:
    print(i)