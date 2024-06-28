from itertools import combinations_with_replacement, permutations
from heapq import heappush, heappop
k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]

def waiting_time(li, num):    # 상담 유형별 시작-종료 시간 리스트, 상담원 숫자
    total_time = 0
    heap = []
    for i in range(num):    # 상담원 숫자만큼 칸 생성
        heappush(heap, 0)

    for start, end in li:
        temp = heappop(heap)
        if start > temp:
            heappush(heap, end)
        else:
            waiting_time = temp - start
            total_time += waiting_time
            heappush(heap, end + waiting_time)
    return total_time

def divid(n, m):
    a = set()
    for j in combinations_with_replacement([i for i in range(1, n-m+2)], r=m):
        if sum(j) == n:
            for k in permutations(j, m):
                a.add(k)
    return a

def solution(k, n, reqs):    # k는 상담 유형 수, n은 멘토의 수, reqs는 상담 요청
    answer = 1e10
    consultant = divid(n, k)
    waiting = [[] for _ in range(k)]

    for req in reqs:    # 상담유형별 대기열
        waiting[req[2]-1].append([req[0], req[0]+req[1]])

    for con in consultant:    # 상담원 경우의 수
        temp = 0
        for j in range(k):    # 삼담 유형별로 계산
            temp += waiting_time(waiting[j], con[j])
        answer = min(answer, temp)
    return answer

solution(k, n, reqs)