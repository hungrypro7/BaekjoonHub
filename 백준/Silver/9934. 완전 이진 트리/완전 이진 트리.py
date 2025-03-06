k = int(input())
inorder = list(map(int, input().split()))

ans = [[] for _ in range(k)]

def dfs(inorder, depth):

    mid = (len(inorder) // 2)

    ans[depth].append(inorder[mid])

    if len(inorder) == 1:
        return

    dfs(inorder[:mid], depth+1)
    dfs(inorder[mid+1:], depth+1)

dfs(inorder, 0)
for i in ans:
    print(*i)