n = int(input())
stack = []
exp = input()
num = []
for i in range(n):
    num.append(int(input()))
for i in exp:
    if 65 <= ord(i) <= 90:
        stack.append(num[ord(i)-65])
    elif i == '+':
        b = stack.pop()
        a = stack.pop()
        temp = a + b
        stack.append(temp)
    elif i == '-':
        b = stack.pop()
        a = stack.pop()
        temp = a - b
        stack.append(temp)
    elif i == '*':
        b = stack.pop()
        a = stack.pop()
        temp = a * b
        stack.append(temp)
    elif i == '/':
        b = stack.pop()
        a = stack.pop()
        temp = a / b
        stack.append(temp)
print("{:.2f}".format(stack[0]))