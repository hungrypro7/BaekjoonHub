import sys
input = sys.stdin.readline
t = int(input())
z = [1, 0, 1]  # 0
o = [0, 1, 1]  # 1
for i in range(t):
    n = int(input())
    if n >= 3:
        for j in range(n-2):
            temp = z[-1] + z[-2]
            z.append(temp)
            temp = o[-1] + o[-2]
            o.append(temp)
    print(z[n], o[n])