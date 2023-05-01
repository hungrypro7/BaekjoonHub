N = int(input())
for i in range(N):
    a1, a2 = map(str, input().split())
    s1 = ''.join(sorted(a1))
    s2 = ''.join(sorted(a2))
    if s1 == s2:
        print("Possible")
    else:
        print("Impossible")