n = int(input())    # 전체 사람의 수
p1, p2 = map(int, input().split())
m = int(input())    # 부모 자식들 간의 관계 수
relation = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False

def dfs(s, cnt):
    global count, arrive
    visited[s] = True
    cnt += 1

    if s == p2:
        print(cnt-1)
        arrive = True
        return

    for j in relation[s]:
        if not visited[j]:
            dfs(j, cnt)

for i in range(m):
    parent, child = map(int, input().split())    # 부모의 자식 간의 관계

    relation[parent].append(child)
    relation[child].append(parent)

dfs(p1, 0)
if arrive == False:
    print(-1)