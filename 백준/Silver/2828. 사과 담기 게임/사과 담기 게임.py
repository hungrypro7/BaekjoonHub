n, m = map(int, input().split())
j = int(input())
result = [0] * (n+1)
distance = 0
left = 1
right = left+m-1
for i in range(j):
    num_of_apple = int(input())
    result[num_of_apple] = 1
    move = 0
    if 1 in result[left:right+1]:
        distance += 0
    elif num_of_apple > right:
        move += num_of_apple - right
        distance += move
        right += move
        left = right - m + 1
    elif num_of_apple < left:
        move += left - num_of_apple
        distance += move
        left -= move
        right = left + m - 1
    result[num_of_apple] = 0
print(distance)