test_case = 10
for i in range(1, test_case+1):
    num_dump = int(input())
    box = list(map(int, input().strip().split(' ')))
    diff = 0

    for j in range(num_dump):
        max_element = max(box)
        index1 = box.index(max_element)
        box[index1] -= 1
        
        min_element = min(box)
        index2 = box.index(min_element)
        box[index2] += 1
        
    diff = max(box) - min(box)
        
    ans = '#' + str(i)
    print(ans, diff)