# append(), pop()의 시간 복잡도는 O(1)이지만 insert()의 시간 복잡도는 O(N)이다.
# 이 문제의 concept : cursor 위치를 기준으로 왼쪽 문자열을 cursor_left, 오른쪽 문자열을 cursor_right로 나눈다.

import sys
cursor_left = list(input())
M = int(input())
cursor_right = []

for i in range(M):
    cm = sys.stdin.readline().split()       # 명령어, 문자 입력받음
    if cm[0] == 'L' and cursor_left:                # 왼쪽 문자열이 있을 때
        cursor_right.append(cursor_left.pop())
    elif cm[0] == 'D' and cursor_right:             # 오른쪽 문자열이 있을 때
        cursor_left.append(cursor_right.pop())
    elif cm[0] == 'B' and cursor_left:              # 삭제할 왼쪽 문자가 있을 때
        cursor_left.pop()
    elif cm[0] == 'P':                              # 문자 추가
        cursor_left.append(cm[1])

print("".join(cursor_left + list(reversed(cursor_right))))
