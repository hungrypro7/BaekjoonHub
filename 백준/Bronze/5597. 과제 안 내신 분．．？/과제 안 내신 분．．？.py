import sys
input = sys.stdin.readline
student = [0] * 30
for i in range(28):
    attend = int(input())
    student[attend-1] = 1
for idx, j in enumerate(student):
    if j == 0:
        print(idx+1)