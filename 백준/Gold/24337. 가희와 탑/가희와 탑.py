n, a, b = map(int, input().split())
ans = []
if a + b > n+1:
    ans.append(-1)
else:
    if a >= b:
        for i in range(1, a+1):
            ans.append(str(i))
        for i in range(n-(a+b)+1):
            ans.insert(0, ans[0])
        for i in range(b-1, 0, -1):
            ans.append(str(i))
    else:
        if a >= 2:
            for i in range(b, 0, -1):
                ans.append(str(i))
            for i in range(a-1, 0, -1):
                ans.insert(0, str(i))
            for i in range(n-len(ans)):
                ans.insert(0, ans[0])
        else:
            for i in range(b-1, 0, -1):
                ans.append(str(i))
            for i in range(n-1-len(ans)):
                ans.insert(0, 1)
            ans.insert(0, b)
print(' '.join(str(_) for _ in ans))