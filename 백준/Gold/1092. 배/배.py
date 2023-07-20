import sys
input = sys.stdin.readline
n = int(input())    # 크레인 개수
crane = list(map(int, input().split()))
m = int(input())    # 박스 개수
box = list(map(int, input().split()))
crane.sort()
box.sort()
minute = 0
if box[-1] > crane[-1]:
    minute = -1
    print(minute)
    sys.exit()
while box:
    temp = len(box)-1
    for i in range(n-1, -1, -1):    # 크레인 탐색
        for j in range(temp, -1, -1):     # 박스 탐색
            if box[j] <= crane[i]:
                box.pop(j)
                temp = j-1
                break
    minute += 1
print(minute)