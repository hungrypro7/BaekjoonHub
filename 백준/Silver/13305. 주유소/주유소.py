N = int(input())    # 도시의 개수
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
money = 0
a, i = 0, 0
while(i < N):
    state = False
    for j in range(i+1, N):
        if costs[i] >= costs[j]:
            money += costs[i] * sum(distances[i:j])
            state = True
            a = j
            break
    if state:
        i = a
    else:
        i += 1

print(money)