s = input()
t = input()
possible = False
def DFS(n, arr):
    global possible
    if n == len(s):
        if arr == s:
            possible = True
        return

    if arr[-1] == 'A':
        arr = arr[:-1]
        DFS(n-1, arr)
        arr += 'A'

    if arr[0] == 'B':
        arr = arr[::-1]
        arr = arr[:-1]
        DFS(n-1, arr)
        arr += 'B'
        arr = arr[::-1]

DFS(len(t), t)
if possible:
    print(1)
else:
    print(0)