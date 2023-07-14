s = input()
t = input()
state = False
def dfs(a, num):
    global state
    if num == len(s):
        if s == a:
            state = True
        return
    if a[-1] == 'A':
        a = a[:-1]
        dfs(a, num-1)
        a += 'A'
    if a[0] == 'B':
        a = a[1:]
        a = a[::-1]
        dfs(a, num-1)
        a += 'B'
        a = a[::-1]

dfs(t, len(t))
if state:
    print(1)
else:
    print(0)