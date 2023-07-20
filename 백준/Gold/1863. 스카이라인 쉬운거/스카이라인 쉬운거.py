import sys
input = sys.stdin.readline
n = int(input())
buildings = []
for i in range(n):
    x, y = map(int, input().split())
    buildings.append(y)
buildings.append(0)
count = 0
stack = []
for i in buildings:
    if stack and stack[-1] > i:
        t = i
        while stack and stack[-1] > i:
            if stack[-1] > i:
                if t != stack[-1]:
                    count += 1
                t = stack[-1]
                stack.pop()
    stack.append(i)
print(count)