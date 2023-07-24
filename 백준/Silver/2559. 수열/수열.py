n, k = map(int, input().split())
temp = list(map(int, input().split()))
accu = sum(temp[:k])
ans = max(accu, -10e10)
for i in range(k, n):
    accu -= temp[i-k]
    accu += temp[i]
    ans = max(accu, ans)
print(ans)