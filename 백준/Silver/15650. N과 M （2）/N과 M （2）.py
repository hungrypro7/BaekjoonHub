import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())

def backTracking(lst, co):
    if len(lst) == m:
        print(*lst)

    for i in range(co, n + 1):
        if i not in lst:
            lst.append(i)
            backTracking(lst, i+1)
            lst.pop()

backTracking([], 1)