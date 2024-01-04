import sys
input = sys.stdin.readline
gear = list(map(int, input().split()))
if gear[0] == 1:
    for i in range(8):
        if gear[i] != i+1:
            print('mixed')
            sys.exit(0)
    print('ascending')
elif gear[0] == 8:
    for i in range(8):
        if gear[i] != 8-i:
            print('mixed')
            sys.exit(0)
    print('descending')
else:
    print('mixed')