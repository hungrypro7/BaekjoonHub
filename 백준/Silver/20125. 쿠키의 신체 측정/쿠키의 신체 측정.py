import sys
input = sys.stdin.readline
n = int(input())
heart_x, heart_y = 0, 0
head = False
left_arm, right_arm = '', ''     # 왼쪽 팔, 오른쪽 팔
waist = ''                       # 허리
left_leg, right_leg = '', ''     # 왼쪽 다리, 오른쪽 다리
leg = False
left, right = 0, 0
for i in range(n):
    data = list(input())
    if data.count('*') == 1 and (not head):
        heart_x, heart_y = i+2, data.index('*')+1
        head = True
    elif data.count('*') >= 3:
        for j in range(heart_y-1):
            if data[j] == '*':
                left_arm += '*'
        for j in range(heart_y, n):
            if data[j] == '*':
                right_arm += '*'
    elif data.count('*') == 1 and head:
        if leg:
            if data.index('*') == left:
                left_leg += '*'
            elif data.index('*') == right:
                right_leg += '*'
        else:
            waist += '*'
    elif data.count('*') == 2 and (not leg):
        leg = True
        left_leg += '*'
        right_leg += '*'
        left = data.index('*')
        right = left + 2
    elif data.count('*') == 2 and leg:
        left_leg += '*'
        right_leg += '*'

print(heart_x, heart_y)
print(len(left_arm), len(right_arm), len(waist), len(left_leg), len(right_leg))