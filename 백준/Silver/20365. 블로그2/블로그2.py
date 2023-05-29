N = int(input())
string = input()
result = 1
B_set = list(string.split('R'))
R_set = list(string.split('B'))
B_set = [v for v in B_set if v]
R_set = [v for v in R_set if v]
if len(B_set) >= len(R_set):
    result += len(R_set)
else:
    result += len(B_set)
print(result)