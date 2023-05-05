N = int(input())
data = list(map(int, input().split()))
stack = []
result = [0] * (N)
for i in range(len(data)):
    while stack:
        if stack[-1][1] < data[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0]
            break
    stack.append([i+1, data[i]])

for i in result:
    print(i, end=' ')