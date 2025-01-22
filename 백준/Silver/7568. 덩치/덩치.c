#include <stdio.h>

typedef struct {
    int weight;
    int height;
} WH;

WH wh[51];

int main(void) {
    
    int n;
    scanf("%d", &n);        // 사람의 수

    for (int i = 0 ; i < n; i++) {
        scanf("%d %d", &wh[i].weight, &wh[i].height);
    }

    int rank[51] = { 0 };
    for (int i = 0; i < n; i++) {
        int r = 0;
        for (int j = 0; j < n; j++) {
            if (i == j) { continue; }

            if (wh[i].weight < wh[j].weight && wh[i].height < wh[j].height) {
                r++;
            }
        }
        rank[i] = r;
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", rank[i] + 1);
    }

    return 0;
}