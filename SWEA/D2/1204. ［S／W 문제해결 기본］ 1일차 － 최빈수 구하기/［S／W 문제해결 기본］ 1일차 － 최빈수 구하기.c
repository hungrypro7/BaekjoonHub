#include <stdio.h>

int max(int a, int b) {
    if (a > b) { return a; }
    else { return a; }
}

int main(void) {

    int t;
    scanf("%d", &t);

    for (int i=0; i < t; i++) {
        int n;
        scanf("%d", &n);

        int scores[1001];
        int num[101] = { 0, };
        for (int j=0; j < 1000; j++) {
            scanf("%d", &scores[j]);
            num[scores[j]] += 1;
        }
    
        int ans = 0;
        int temp = 0;
        for (int j=0; j < 101; j++) {
            if (temp <= num[j]) {
                temp = num[j];
                ans = j;
            }
        }

        printf("#%d %d\n", n, ans);
    }

    return 0;
}