#include <stdio.h>

int main(void) {
    int n;      // 도시의 개수
    scanf("%d", &n);
    int dis[100000];        // 도시 간의 거리
    int ppl[100000];        // 주유소 리터당 가격
    for (int i = 0; i < n-1; i++) {
        int d;
        scanf("%d", &d);
        dis[i] = d;
    }
    for (int i = 0; i < n; i++) {
        int c;
        scanf("%d", &c);
        ppl[i] = c;
    }
    
    int pt = 0;
    int ans = 0;
    for (int i=1; i < n; i++) {
        if (ppl[i] < ppl[pt] || i == n-1) {
            int temp = 0;   // 거리
            for (int j=pt; j < i; j++) {
                temp += dis[j];
            }
            ans += temp * ppl[pt];
            pt = i;
        }
    }
    printf("%d", ans);
    return 0;
}