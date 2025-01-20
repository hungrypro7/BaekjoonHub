#include <stdio.h>
#include <string.h>

int main(void) {
    
    int m;      // 연산의 수
    scanf("%d", &m);

    char order[10];
    int s[20] = { 0 };    // 집합s
    int x;
    for (int i=0; i < m; i++) {
        
        scanf("%s %d", order, &x);
        
        if (strcmp(order, "add") == 0) {
            s[x-1] = 1;
        }
    
        if (strcmp(order, "remove") == 0) {
            if (s[x-1] == 1) {
                s[x-1] = 0;
            }
        }

        if (strcmp(order, "check") == 0) {
            if (s[x-1] == 1) {
                printf("1\n");
            }
            else {
                printf("0\n");
            }
        }

        if (strcmp(order, "toggle") == 0) {
            if (s[x-1] == 1) {
                s[x-1] = 0;
            }
            else {
                s[x-1] = 1;
            }
        }

        if (strcmp(order, "all") == 0) {
            for (int j=0; j < 20; j++) {
                s[j] = 1;
            }
        }

        if (strcmp(order, "empty") == 0) {
            for (int j=0; j < 20; j++) {
                s[j] = 0;
            }
        }
    }
    return 0;
}