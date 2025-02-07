#include <stdio.h>

int main(void) {
    int height_info[10] = { 0, };
    int n;  // 사람의 수
    scanf("%d", &n);
    for (int i=0; i < n; i++) {
        scanf("%d", &height_info[i]);
    }

    int ans[10] = { 0, };
    for (int i=1; i < n+1; i++) {
        int p = 0;
        for (int j=0; j < 10; j++) {
            if (p == height_info[i-1] && !ans[j]) {
                ans[j] = i;
                break;
            }

            if (!ans[j]) {
                p++;
            }
        }
    }

    for (int i=0; i < n; i++) {
        printf("%d ", ans[i]);
    }

    return 0;
}