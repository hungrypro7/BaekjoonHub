#include <stdio.h>
#include <math.h>

int main(void) {
    int t;
    scanf("%d", &t);
    
    int x1, y1, r1, x2, y2, r2;
    double distance;
    
    for(int i=0; i<t; i++) {
        
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        distance = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1- y2));
        
        if (distance == 0) {
            if (r1 == r2) {
                printf("-1\n");
            }
            else {
                printf("0\n");
            }
        }
        else {
            if (r1 + r2 > distance) {
                if (fabs(r1 - r2) > distance) {
                    printf("0\n");
                }
                else if (fabs(r1 - r2) == distance) {
                    printf("1\n");
                }
                else {
                    printf("2\n");
                }
            } else if (r1 + r2 == distance) {
                printf("1\n");
            } else {
                printf("0\n");
            }
        }
    }
    return 0;
}
