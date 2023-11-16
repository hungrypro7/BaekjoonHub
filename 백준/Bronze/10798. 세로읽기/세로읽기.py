words = []
length = 0
for i in range(5):
    temp = list(input())
    words.append(temp)
    if len(temp) >= length:
        length = len(temp)
        
for j in range(length):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')
