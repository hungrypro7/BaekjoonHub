n = int(input())
pattern = list(input().split('*'))
start, end = pattern[0], pattern[1]
for i in range(n):
    file = input()
    if len(start) + len(end) > len(file):
        print('NE')
    else:
        if start == file[:len(start)] and end == file[-len(end):]:
            print('DA')
        else:
            print('NE')