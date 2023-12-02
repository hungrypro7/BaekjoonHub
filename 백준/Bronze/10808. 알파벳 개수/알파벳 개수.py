alp = [0] * 26
exp = input()
for i in exp:
    alp[ord(i)-97] += 1
print(*alp)