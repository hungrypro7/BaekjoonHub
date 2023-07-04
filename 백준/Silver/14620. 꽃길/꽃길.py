N = int(input())
land = []
for i in range(N):
    land.append(list(map(int, input().split())))
cost = []
for i in range(1, N-1):
    for j in range(1, N-1):
        cost.append((land[i][j] + land[i-1][j] + land[i+1][j] + land[i][j-1] + land[i][j+1], i, j))

cost.sort()
def dfs(visited, total):
    global ans
    if total > ans: return
    if len(visited) == 15:
        ans = min(ans, total)
    else:
        for j in cost:
            if ([j[1], j[2]+1] not in visited) and ([j[1], j[2]-1] not in visited) and ([j[1]+1, j[2]] not in visited) and ([j[1]-1, j[2]] not in visited):
                temp = [[j[1], j[2]]]
                temp.append([j[1], j[2]+1])
                temp.append([j[1], j[2]-1])
                temp.append([j[1]+1, j[2]])
                temp.append([j[1]-1, j[2]])
                temp_cost = j[0]
                dfs(visited + temp, total + temp_cost)

ans = 100000000000
dfs([], 0)
print(ans)