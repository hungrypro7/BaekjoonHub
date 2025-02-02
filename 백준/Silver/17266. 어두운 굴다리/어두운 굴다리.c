#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    if (a > b) { return a; }
    else { return b; }
}

int main(void) {
    int n;      // 굴다리의 길이
    scanf("%d", &n);

    int m;      // 가로등의 개수
    scanf("%d", &m);

    int* place;
    place = (int *)malloc(sizeof(int) * (m+1));

    place[0] = 0;
    for (int i = 0; i < m; i++) {
        int a;
        scanf("%d", &a);
        place[i+1] = a;
    }

    int ans = place[1] - place[0];
    for (int i=1; i < m-1; i++) {
        int temp;
        if ((place[i] - place[i-1]) % 2 == 0) {
            temp = (int)((place[i] - place[i-1]) / 2);
        }
        else {
            temp = (int)((place[i] - place[i-1]) / 2) + 1;
        }
        ans = max(ans, temp);
    }

    ans = max(ans, n - place[m]);

    printf("%d", ans);

    free(place);
}