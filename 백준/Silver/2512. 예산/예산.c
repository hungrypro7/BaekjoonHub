#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int max(int a, int b) {
    if (a > b) { return a; }
    else { return b; }
}

int main(void) {
    int n;     // 지방의 수
    scanf("%d", &n);

    int afm[100001];    // 예산 요청
    for (int i=0; i < n; i++) {
        scanf("%d", &afm[i]);
    }

    int total_money;    // 총 예산
    scanf("%d", &total_money);

    qsort(afm, n, sizeof(afm[0]), compare);

    int temp = 0;
    int ans = 0;

    for (int i=0; i < n; i++) {
        if ((temp + afm[i] * (n - i)) > total_money) {
            ans = max(ans, (int)((total_money - temp) / (n-i)));
            break;
        }
        temp += afm[i];
        ans = afm[i];
    }

    printf("%d", ans);
    return 0;
}