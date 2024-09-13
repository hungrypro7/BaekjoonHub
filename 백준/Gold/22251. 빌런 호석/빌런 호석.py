n, k, p, x = map(int, input().split())    # 층, 디스플레이 자리 수, 반전시킬 최대 개수, 현재 층
led = [[1, 1, 1, 0, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 0],
       [1, 0, 1, 1, 1, 0, 1],
       [1, 0, 1, 1, 0, 1, 1],
       [0, 1, 1, 1, 0, 1, 0],
       [1, 1, 0, 1, 0, 1, 1],
       [1, 1, 0, 1, 1, 1, 1],
       [1, 0, 1, 0, 0, 1, 0],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1]
    ]

def compare(a, b):
    count = 0
    str1, str2 = str(a), str(b)
    len1, len2 = len(str1), len(str2)

    if len1 == len2:

        for j in range(-1, -len1-1, -1):
            temp1, temp2 = int(str1[j]), int(str2[j])
            for k in range(7):
                if led[temp1][k] != led[temp2][k]:
                    count += 1

    elif len1 > len2:
        str2 = ('0' * (len1 - len2)) + str2
        for j in range(-1, -len1-1, -1):
            temp1, temp2 = int(str1[j]), int(str2[j])
            for k in range(7):
                if led[temp1][k] != led[temp2][k]:
                    count += 1

    else:
        str1 = ('0' * (len2 - len1)) + str1
        for j in range(-1, -len2-1, -1):
            temp1, temp2 = int(str1[j]), int(str2[j])
            for k in range(7):
                if led[temp1][k] != led[temp2][k]:
                    count += 1

    return count

ans = 0
for i in range(1, n+1):
    if i != x and compare(i, x) <= p:
       ans += 1

print(ans)