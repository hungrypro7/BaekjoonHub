import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())   # 벨트 길이, 0인 칸의 개수 제한
conveyer = deque(list(map(int, input().split())))   # 칸의 내구도
step = 0
robot = deque([0] * n)

while conveyer.count(0) < k:
    conveyer.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0

    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and conveyer[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            conveyer[i+1] -= 1
    robot[-1] = 0

    if robot[0] != 1 and conveyer[0] > 0:
        robot[0] = 1
        conveyer[0] -= 1

    step += 1   # 단계 1 증가

print(step)