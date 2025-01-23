#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp (const void *a, const void *b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

int main(void) {

    int n;
    char g;
    scanf("%d %c", &n, &g);

    char* name[100000];
    for (int i=0; i < n; i++) {
        name[i] = malloc(21 * sizeof(char));
        scanf("%s", name[i]);
    }

    qsort(name, n, sizeof(name[0]), cmp);

    int cnt = 1;
    for(int i=0; i < n-1; i++) {
        if (strcmp(name[i], name[i+1]) != 0) {
            cnt++;
        }
    }

    int ans;
    if (g == 'Y') {
        ans = cnt;
    }
    else if (g == 'F') {
        ans = cnt / 2;
    }
    else if (g == 'O') {
        ans = cnt / 3;
    }

    printf("%d", ans);

    for(int i=0; i < n; i++) {
        free(name[i]);
    }

    return 0;
}