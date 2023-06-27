n = int(input())
eureca = []
for j in range(1, 46):
    eureca.append(j * (j + 1) // 2)

def triangle(a):
    for p in range(45):
        for q in range(p, 45):
            for r in range(q, 45):
                if eureca[p] + eureca[q] + eureca[r] == a:
                    return 1
    return 0

for i in range(n):
    case = int(input())
    print(triangle(case))