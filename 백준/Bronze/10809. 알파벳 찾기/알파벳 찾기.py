s = input()
alp = [-1] * 26
for idx, j in enumerate(s):
    if alp[ord(j)-97] == -1:
        alp[ord(j)-97] = idx
print(*alp)