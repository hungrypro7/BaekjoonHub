n, k = map(int, input().split())
num = input()
stack = []
count = 0
p = 0
while p != n:
    stack.append(num[p])
    if (p < n-1 and stack[-1] < num[p+1]) or (p == n-1 and count < k):
        while stack and count < k:
            if p == n-1 or stack[-1] < num[p+1]:
                stack.pop()
                count += 1
            else:
                break
    p += 1
print(''.join(str(_) for _ in stack))