import sys
T = int(input())    # 테스트 케이스

num = {0 : [1, 1, 1, 0, 1, 1, 1], 
       1 : [0, 0, 0, 0, 0, 1, 1], 
       2 : [0, 1, 1, 1, 1, 1, 0], 
       3 : [0, 0, 1, 1, 1, 1, 1], 
       4 : [1, 0, 0, 1, 0, 1, 1], 
       5 : [1, 0, 1, 1, 1, 0, 1], 
       6 : [1, 1, 1, 1, 1, 0, 1], 
       7 : [1, 0, 1, 0, 0, 1, 1], 
       8 : [1, 1, 1, 1, 1, 1, 1], 
       9 : [1, 0, 1, 1, 1, 1, 1]}

for i in range(T):
    ans = 0
    a, b = map(str, input().split())    # 전, 후

    if len(a) == len(b):
        for j in range(len(a)):
            num1, num2 = int(a[j]), int(b[j])
            for k in range(7):
                if num[num1][k] != num[num2][k]:
                    ans += 1
                    
    elif len(a) > len(b):
        for j in range(-1, -len(b)-1, -1):
            num1, num2 = int(a[j]), int(b[j])
            for k in range(7):
                if num[num1][k] != num[num2][k]:
                    ans += 1
                    
        temp = len(a) - len(b)

        for j in range(temp):
            num1 = int(a[j])
            ans += sum(num[num1])
            
    elif len(a) < len(b):
        for j in range(-1, -len(a)-1, -1):
            num1, num2 = int(a[j]), int(b[j])
            for k in range(7):
                if num[num1][k] != num[num2][k]:
                    ans += 1

        temp = len(b) - len(a)

        for j in range(temp):
            num1 = int(b[j])
            ans += sum(num[num1])
            
    print(ans)
