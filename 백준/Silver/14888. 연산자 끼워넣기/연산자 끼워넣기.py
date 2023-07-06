n = int(input())
number = list(map(int, input().split()))
o1, o2, o3, o4 = map(int, input().split())  # 덧셈, 뺄셈, 곱셈, 나눗셈
max_result = -1e10
min_result = 1e10

def DFS(num, arr):
    global o1, o2, o3, o4, max_result, min_result

    if num == n-1:
        max_result = max(max_result, arr)
        min_result = min(min_result, arr)

    if o1 > 0:
        o1 -= 1
        DFS(num+1, arr+number[num+1])
        o1 += 1
    if o2 > 0:
        o2 -= 1
        DFS(num+1, arr-number[num+1])
        o2 += 1
    if o3 > 0:
        o3 -= 1
        DFS(num+1, arr * number[num+1])
        o3 += 1
    if o4 > 0:
        o4 -= 1
        DFS(num+1, int(arr / number[num+1]))
        o4 += 1

DFS(0, number[0])
print(max_result)
print(min_result)