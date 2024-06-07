import sys
n = int(input())    # 격자 크기
tree = []
for i in range(n):
    tree.append(list(map(int, input().split())))

ans = 0
visited = [[0] * 4 for _ in range(4)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def backtrack(cnt, beauty):
    global ans, temp
    if cnt == temp:
        ans = max(ans, beauty)
        return 

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:    # 방문하지 않았다면
                visited[i][j] = 1

                for k in range(4):
                    nx = i + dx[k] 
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == 0:    # 방문하지 않았다면
                            visited[nx][ny] = 1
                            backtrack(cnt+1, beauty+tree[i][j]+tree[nx][ny])
                            visited[nx][ny] = 0
            
                visited[i][j] = 0
if n == 2:
    temp = 2
else:
    temp = 4

backtrack(0, 0)
print(ans)
