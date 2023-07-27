n = int(input())
fn = [1, 1]
for i in range(2, n+1):
    a = fn[i-1] + (2 * fn[i-2])
    fn.append(a)

if n == 1:
    ans = n
elif n % 2 == 0:
    ans = (fn[n]-(fn[n//2]+2*fn[(n-2)//2]))//2 + (fn[n//2]+2*fn[(n-1)//2])
elif n % 2 == 1:
    ans = (fn[n]-(fn[(n-1)//2]))//2 + fn[(n-1)//2]
print(ans)