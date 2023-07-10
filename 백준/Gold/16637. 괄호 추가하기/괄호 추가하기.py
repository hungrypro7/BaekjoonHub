n = int(input())
exp = input()
ans = -2 ** 31 + 1

def op(num1, ope, num2):
    num1 = int(num1)
    num2 = int(num2)
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2

def DFS(idx, result):
    global ans
    if idx == n-1:
        ans = max(ans, result)
        return

    if idx + 2 < n:
        DFS(idx+2, op(result, exp[idx+1], exp[idx+2]))

    if idx + 4 < n:
        DFS(idx+4, op(result, exp[idx+1], op(exp[idx+2], exp[idx+3], exp[idx+4])))

DFS(0, int(exp[0]))
print(ans)