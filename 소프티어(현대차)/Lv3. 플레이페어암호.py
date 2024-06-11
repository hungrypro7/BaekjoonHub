import sys
message = input()  # 메세지
key = input()  # 키
message_length = len(message)
key_length = len(key)

# 1. cipher 만들기
cipher = [[] for _ in range(5)]
alphabet = [0] * 26
alphabet[74 - 65] = 1  # J에 체크
temp1, temp2 = 0, 0  # 문자 포인터, cipher 열 포인터
for i in range(key_length):
    if alphabet[ord(key[i]) - 65] == 0:
        alphabet[ord(key[i]) - 65] = 1
        cipher[temp2].append(key[i])
        temp1 += 1

        if temp1 % 5 == 0:
            temp2 += 1

for i in range(26):
    if alphabet[i] == 0:
        cipher[temp2].append(chr(i + 65))
        temp1 += 1

        if temp1 % 5 == 0:
            temp2 += 1

# 2. 메세지 두 글자씩 나누기
mes_split = []
po = 0
while po < message_length:
    temp = []
    if po == message_length - 1:
        temp.append(message[po] + 'X')
        po += 1
    elif message[po] != message[po + 1]:
        temp.append(message[po] + message[po + 1])
        po += 2
    elif message[po] == message[po + 1]:
        if message[po] == 'X':
            temp.append(message[po] + 'Q')
        else:
            temp.append(message[po] + 'X')
        po += 1
    mes_split.append(temp)

# 3. 매칭 시키기
ans = ''
x1, y1, x2, y2 = 0, 0, 0, 0
for i in mes_split:
    st1, st2 = i[0][0], i[0][1]
    for k in range(5):
        for j in range(5):
            if cipher[k][j] == st1:
                x1, y1 = k, j
            if cipher[k][j] == st2:
                x2, y2 = k, j

    if x1 == x2:    # 1. 두 글자가 같은 행에 존재하면
        ans += cipher[x1][(y1+1)%5]
        ans += cipher[x2][(y2+1)%5]
    elif y1 == y2:    # 2. 두 글자가 같은 열에 존재하면
        ans += cipher[(x1+1)%5][y1]
        ans += cipher[(x2+1)%5][y2]
    else:    # 3. 두 글자가 서로 다른 행, 열에 존재하면
        ans += cipher[x1][y2]
        ans += cipher[x2][y1]

print(ans)
