#include <stdio.h>

int main(void) {
    int h, w, n, m;     // 열, 행, 세로 비우는 칸 개수, 가로 비우는 칸 개수

    scanf("%d %d %d %d", &h, &w, &n, &m);

    int col, row;

    if (h % (n+1) == 0) {
        col = h / (n + 1);
    } else {
        col = h / (n + 1) + 1;
    }

    if (w % (m+1) == 0) {
        row = w / (m + 1);
    } else {
        row = w / (m + 1) + 1;
    }

    printf("%d", col * row);

    return 0;
}