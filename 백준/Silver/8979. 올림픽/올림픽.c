#include <stdio.h>

typedef struct {
    int num;
    int gold;
    int silver;
    int bronze;
} MEDAL;

MEDAL medal[1001];

int main(void) {
    
    int n, k;
    scanf("%d %d", &n, &k);       // 국가의 수, 등수를 알고 싶은 국가

    int target = 0;     // target index
    for (int i = 0; i < n; i++) {

        scanf("%d %d %d %d", &medal[i].num, &medal[i].gold, &medal[i].silver, &medal[i].bronze);

        if (medal[i].num == k) {
            target = i;
        }
    }

    int rank = 0;

    for (int i = 0; i < n; i++) {

        if (i != target) {
            if (medal[i].gold > medal[target].gold) {
                rank++;
            }
            else if (medal[i].gold == medal[target].gold) {
                if (medal[i].silver > medal[target].silver) {
                    rank++;
                }
                else if (medal[i].silver == medal[target].silver) {
                    if (medal[i].bronze > medal[target].bronze) {
                        rank++;
                    }
                }
            }
        }

    }

    printf("%d\n", rank + 1);

    return 0;
}