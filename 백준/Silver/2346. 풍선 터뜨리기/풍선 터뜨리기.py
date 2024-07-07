from collections import deque
n = int(input())    # 풍선 개수
balloon = list(map(int, input().split()))
deq = deque([i for i in range(n, 0, -1)])
new_ans = []
point = 0
move = 0
a = deq.pop()
new_ans.append(a)    # 1 추가
while deq:
    move = balloon[point]
    if move > 0:
        for i in range(move-1):
            a = deq.pop()
            deq.appendleft(a)
        a = deq.pop()
        new_ans.append(a)
        point = a-1
    else:
        for i in range(abs(move)-1):
            a = deq.popleft()
            deq.append(a)
        a = deq.popleft()
        new_ans.append(a)
        point = a-1
print(*new_ans)