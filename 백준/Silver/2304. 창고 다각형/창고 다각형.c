#include <stdio.h>

int main(void) {
    int n;  // 기둥의 개수
    scanf("%d", &n);
    int h[1001] = { 0, };
    int max_height = 0;
    for (int i=0; i < n; i++) {
        int pos, height;
        scanf("%d %d", &pos, &height);
        h[pos] = height;
        if (height > max_height) {
            max_height = height;
        }
    }

    // 0부터 시작
    int ans = 0;
    int temp_max1 = 0;
    int ind1 = 0;
    for (int i=0; i < 1001; i++) {
        if (h[i] == max_height) {
            ind1 = i;
            break;
        }
        if (h[i] > temp_max1) {
            temp_max1 = h[i];
        }
        ans += temp_max1;
    }

    // 1000 에서 시작 (거꾸로)
    int temp_max2 = 0;
    int ind2 = 0;
    for (int i=1000; i > -1; i--) {
        if (h[i] == max_height) {
            ind2 = i;
            break;
        }
        if (h[i] > temp_max2) {
            temp_max2 = h[i];
        }
        ans += temp_max2;
    }

    ans += (ind2 - ind1 + 1) * max_height;
    printf("%d\n", ans);
    return 0;
}