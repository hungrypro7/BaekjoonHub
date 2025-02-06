#include <stdio.h>

int main(void) {
    int t;    // 테스트 케이스 개수
    scanf("%d", &t);

    while (t--) {
        int days;
        scanf("%d", &days);

        int stock[1000001];
        for (int i = 0; i < days; i++) {
            scanf("%d", &stock[i]);
        }

        long long benefit = 0;
        int max_price = 0;

        // 뒤에서부터 순회하면서 최대 가격 갱신
        for (int i = days - 1; i >= 0; i--) {
            if (stock[i] > max_price) {
                max_price = stock[i];
            } else {
                benefit += (max_price - stock[i]);
            }
        }

        printf("%lld\n", benefit);
    }
    return 0;
}
