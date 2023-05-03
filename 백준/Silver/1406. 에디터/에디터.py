import sys
cursor_left = list(input())
M = int(input())
cursor_right = []

for i in range(M):
    cm = sys.stdin.readline().split()       # 명령어, 문자 입력받음
    if cm[0] == 'L' and cursor_left:
        cursor_right.append(cursor_left.pop())
    elif cm[0] == 'D' and cursor_right:      # cursor가 문장의 맨 뒤가 아닐 때
        cursor_left.append(cursor_right.pop())
    elif cm[0] == 'B' and cursor_left:
        cursor_left.pop()
    elif cm[0] == 'P':
        cursor_left.append(cm[1])

print("".join(cursor_left + list(reversed(cursor_right))))