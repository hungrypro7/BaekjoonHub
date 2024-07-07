from collections import deque
n, k = map(int, input().split())
circle = [i for i in range(n, 0, -1)]
circle = deque(circle)
new_circle = []
point = 1
while circle:
	a = circle.pop()
	if point % k == 0:
		new_circle.append(a)
		point = 1
	else:
		circle.appendleft(a)
		point += 1
print('<', end='')
print(*new_circle, sep=', ', end='')
print('>')