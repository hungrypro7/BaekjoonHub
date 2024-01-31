n, m = map(int, input().split())
count = [[0, 0, 0, 0] for _ in range(m)]    # A C G T
for i in range(n):
    dna = input()
    for j in range(m):
        if dna[j] == 'A':
            count[j][0] += 1
        elif dna[j] == 'C':
            count[j][1] += 1
        elif dna[j] == 'G':
            count[j][2] += 1
        elif dna[j] == 'T':
            count[j][3] += 1

ans = ''
hamming_distance = 0
for i in count:
    if i.index(max(i)) == 0:
        ans += 'A'
        del i[0]
    elif i.index(max(i)) == 1:
        ans += 'C'
        del i[1]
    elif i.index(max(i)) == 2:
        ans += 'G'
        del i[2]
    elif i.index(max(i)) == 3:
        ans += 'T'
        del i[3]
    hamming_distance += sum(i)

print(ans)
print(hamming_distance)