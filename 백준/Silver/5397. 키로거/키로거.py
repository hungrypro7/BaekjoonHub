n = int(input())
for i in range(n):
    key = input()
    cursor_left = []
    cursor_right = []
    for j in range(len(key)):
        if key[j] == "<" and cursor_left:
            cursor_right.append(cursor_left.pop())
        elif key[j] == ">" and cursor_right:
            cursor_left.append(cursor_right.pop())
        elif key[j] == "-" and cursor_left:
            cursor_left.pop()
        elif key[j] != "<" and key[j] != ">" and key[j] != "-":
            cursor_left.append(key[j])

    print("".join(cursor_left + list(reversed(cursor_right))))