N = int(input())
building = []
stack = []
counter = 0
for i in range(N):
    floor = int(input())
    building.append(floor)

for j in building:
    while stack and stack[-1] <= j:
        stack.pop()
    stack.append(j)

    counter += len(stack)-1

print(counter)