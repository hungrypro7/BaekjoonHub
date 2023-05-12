n = int(input())

def print_star(n):
    if n == 1:
        return ['*']

    stars = print_star(n // 3)
    lt = []

    for s in stars:
        lt.append(s*3)
    for s in stars:
        lt.append(s+" "*int(n//3)+s)
    for s in stars:
        lt.append(s*3)

    return lt

print('\n'.join(print_star(n)))