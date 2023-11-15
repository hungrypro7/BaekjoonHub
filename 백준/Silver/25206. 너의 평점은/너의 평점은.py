import sys
input = sys.stdin.readline
gpa = 0
n = 0
for i in range(20):
    sub, major, grade = input().split()
    if grade != 'P':
        n += float(major)
    if grade == 'A+':
        gpa += float(major) * 4.5
    elif grade == 'A0':
        gpa += float(major) * 4.0
    elif grade == 'B+':
        gpa += float(major) * 3.5
    elif grade == 'B0':
        gpa += float(major) * 3.0
    elif grade == 'C+':
        gpa += float(major) * 2.5
    elif grade == 'C0':
        gpa += float(major) * 2.0
    elif grade == 'D+':
        gpa += float(major) * 1.5
    elif grade == 'D0':
        gpa += float(major) * 1.0
    elif grade == 'F':
        gpa += float(major) * 0.0
print("{:.6f}".format(gpa/n))