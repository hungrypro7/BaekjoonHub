Y0, M0, D0, T0, P0 = map(float, input().split())
Y1, M1, D1, T1, P1 = map(float, input().split())

ans_y, ans_m, ans_d, ans_t, ans_p = 0, 0, 0, 0, 0

before = 360 * (int(Y0)) + 30 * (int(M0)-1) + int(D0)
after = 360 * (int(Y1)) + 30 * (int(M1)-1) + int(D1)

if before < after:
    tmp = after - before
    before -= tmp

    ans_y = before // 360
    if (before % 360) == 0:
        ans_y -= 1

    ans_m = (before % 360) // 30
    if (before % 360) == 0:
        ans_m = 12

    ans_d = before % 30
    if ans_d == 0:
        ans_d = 30
    else:
        ans_m += 1

else:
    tmp = before - after
    before += tmp

    ans_y = before // 360
    if (before % 360) == 0:
        ans_y -= 1

    ans_m = (before % 360) // 30
    if (before % 360) == 0:
        ans_m = 12

    ans_d = before % 30
    if ans_d == 0:
        ans_d = 30
    else:
        ans_m += 1

if T0 > T1:
    tmp = T0 - T1
    ans_t = T0 + tmp
else:
    tmp = T1 - T0
    ans_t = T0 - tmp

if P0 > P1:
    tmp = P0 - P1
    ans_p = P0 + tmp
else:
    tmp = P1 - P0
    ans_p = P0 - tmp

print(ans_y, ans_m, ans_d, f"{ans_t:.3f}", f"{ans_p:.3f}")