#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {

    int t;
    scanf("%d", &t);

    char *color[6] = {"red", "orange", "yellow", "green", "blue", "purple"};
    char c1[10];
    char c2[10];
    for (int i=0; i < t; i++) {
        scanf("%s %s", c1, c2);
        
        int c1_idx, c2_idx;
        for (int j=0; j < 6; j++) {
            if (strcmp(color[j], c1) == 0) {
                c1_idx = j;
            }
            if (strcmp(color[j], c2) == 0) {
                c2_idx = j;
            }
        }

        if (c1_idx == c2_idx) {
            printf("E\n");
        }
        else if (abs(c1_idx-c2_idx) == 1 || abs(c1_idx-c2_idx) == 5) {
            printf("A\n");
        }
        else if (abs(c1_idx - c2_idx) == 3) {
            printf("C\n");
        }
        else {
            printf("X\n");
        }
    }   

    return 0;
}