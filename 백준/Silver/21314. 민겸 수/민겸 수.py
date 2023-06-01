mk = input()
a = 0
max_list = []
for i in range(len(mk)):            # 문자열을 쪼개는 과정
    if mk[i] == 'K':
        max_list.append(mk[a:i+1])
        a = i+1
    elif i == len(mk)-1 and mk[i] != 'K':
        for j in mk[a:]:
            max_list.append(j)

m = ''
min_list = []
for i in range(len(mk)):            # 문자열을 쪼개는 과정
    if mk[i] == 'K':
        if i == 0:
            min_list.append(mk[i])
        elif mk[i-1] == 'M':
            min_list.append(m)
            m = ''
            min_list.append(mk[i])
        else:
            min_list.append(mk[i])
    elif i == len(mk) - 1 and mk[i] == 'M':
        m += mk[i]
        min_list.append(m)
    elif mk[i] == 'M':
        m += mk[i]

max_string = ''
for j in max_list:
    if 'K' in j:
        max_string += str(5*10**(len(j)-1))
    else:
        max_string += str(10**(len(j)-1))

min_string = ''
for j in min_list:
    if j == 'K':
        min_string += str(5)
    elif j == 'M':
        min_string += str(1)
    else:
        min_string += str(10**(len(j)-1))

print(max_string)
print(min_string)