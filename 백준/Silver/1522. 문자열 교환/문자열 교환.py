import math
s = input()
a = s.count('a')

s += s[0:a-1]    # 원형 문자열
min_val = math.inf    # 최솟값
for i in range(len(s) - (a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)