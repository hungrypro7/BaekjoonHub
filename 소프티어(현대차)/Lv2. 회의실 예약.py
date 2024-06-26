import sys

n, m = map(int, input().split())  # 회의실 수, 회의 수
meeting_room = {}
for i in range(n):  # 각 회의실 이름이 주어짐
    room_name = input()
    meeting_room[room_name] = [1] * 9

for i in range(m):  # 회의 예약 정보
    room_name, start, end = map(str, input().split())
    s, e = int(start) - 9, int(end) - 9
    for j in range(s, e):
        meeting_room[room_name][j] = 0

count = 0
meeting_room = sorted(meeting_room.items(), key=lambda item: item[0])
for key, value in meeting_room:
    print('Room', end=' ')
    print(key, ':', sep='')
    ans = []
    temp = ''
    if 1 not in value:
        print('Not available')
    else:
        for idx, val in enumerate(value):
            if val == 1 and idx == 0:    # 시작 위치일 때 1
                temp += '09-'
            elif val == 1 and value[idx-1] == 0:    # 시작 위치일 때 2
                temp += str(idx+9) + '-'

            if val == 1 and idx == 8:    # 끝 위치일 때 1
                temp += str(idx+10)
                ans.append(temp)
                temp = ''
            elif val == 1 and value[idx+1] == 0:     # 끝 위치일 때 2
                temp += str(idx+10)
                ans.append(temp)
                temp = ''
        print(len(ans), 'available:')
        for j in ans:
            print(j)
    if count != n-1:
        print('-----')
    count += 1
