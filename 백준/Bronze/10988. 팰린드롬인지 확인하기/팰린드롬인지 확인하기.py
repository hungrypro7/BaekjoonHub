s = input()
state = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        state = False
if state:
    print(1)
else:
    print(0)