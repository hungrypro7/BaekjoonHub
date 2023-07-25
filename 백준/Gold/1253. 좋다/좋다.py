import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
answer = 0

def goodnum(find):
    i = 0
    j = n-1
    while i < j:
        if a[i] + a[j] == find:
            if i != k and j != k:
                return True
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif a[i] + a[j] < find:
            i += 1
        else:
            j -= 1
    return False

a.sort()
for k in range(n):
    if goodnum(a[k]):
        answer += 1

print(answer)