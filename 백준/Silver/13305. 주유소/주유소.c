#include <stdio.h>

int main(void) {
    int n;      // 도시의 개수
    scanf("%d", &n);
    int dis[100000];        // 도시 간의 거리
    long long ppl[100000];  // 주유소 리터당 가격 (long long으로 변경)
    for (int i = 0; i < n-1; i++) {
        int d;
        scanf("%d", &d);
        dis[i] = d;
    }
    for (int i = 0; i < n; i++) {
        long long c;        // long long으로 변경
        scanf("%lld", &c);  // %lld로 변경
        ppl[i] = c;
    }
    
    int pt = 0;
    long long ans = 0;      // long long으로 변경
    for (int i = 1; i < n; i++) {
        if (ppl[i] < ppl[pt] || i == n-1) {
            long long temp = 0;   // 거리 (long long으로 변경)
            for (int j = pt; j < i; j++) {
                temp += dis[j];
            }
            ans += temp * ppl[pt];
            pt = i;
        }
    }
    printf("%lld", ans);    // %lld로 변경
    return 0;
}