#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int card[500000];
    for (int i=0; i < n; i++) {
        card[i] = i+1;
    }
    
    int start = 0;
    int end = n-1;
    while(1) {
        start = (start + 1) % n;
        end = (end + 1) % n;
        card[end] = card[start];
        if (start == end) break;
        start = (start + 1) % n;
        if (start == end) break;
    }
    printf("%d", card[start]);
    return 0;
}