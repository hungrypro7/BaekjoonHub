while True:
    try:
        st = input()
        ans = [0] * 4
        for i in st:
            if 97 <= ord(i) <= 122:
                ans[0] += 1
            elif 65 <= ord(i) <= 90:
                ans[1] += 1
            elif i == ' ':
                ans[3] += 1
            elif 0 <= int(i) <= 9:
                ans[2] += 1
        print(*ans)
    except EOFError:
        break