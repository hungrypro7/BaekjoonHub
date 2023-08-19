import sys
input = sys.stdin.readline
n = int(input())
budgets = list(map(int, input().split()))
nation_budget = int(input())

if sum(budgets) <= nation_budget:
    print(max(budgets))
else:
    budgets = sorted(budgets)
    over = 0
    ans = 0
    for i in range(n):
        ans = budgets[i]
        if ans * (n-i) + over > nation_budget:
            ans = (nation_budget - over) // (n-i)
            break
        over += budgets[i]
    print(ans)