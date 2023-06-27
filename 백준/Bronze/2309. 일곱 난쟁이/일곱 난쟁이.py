dwarves = []
answer = []
state = False
for i in range(9):
    height = int(input())
    dwarves.append(height)
dwarves.sort()
for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarves[:i]) + sum(dwarves[i+1:j]) + sum(dwarves[j+1:]) == 100:
            a = dwarves[:i] + dwarves[i+1:j] + dwarves[j+1:]
            for k in a:
                print(k)
                state = True
            break
    if state:
        break
