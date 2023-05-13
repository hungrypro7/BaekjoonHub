n = int(input())

def write_star(t):
    if t == 1:
        return ['*']

    stars = write_star(t-1)
    list = []

    list.append("*" * (4 * t - 3))
    list.append("*"+" "*(4 * t - 5)+"*")
    for i in stars:
        list.append("* " + i + " *")
    list.append("*" + " " * (4 * t - 5) + "*")
    list.append("*" * (4 * t - 3))

    return list

print('\n'.join(write_star(n)))

