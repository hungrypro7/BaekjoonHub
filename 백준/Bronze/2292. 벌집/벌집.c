#include <stdio.h>

int main(void) {
    
    int n;
    scanf("%d", &n);

    int temp = 1;
    int six_times = 0;
    int cnt = 1;
    while (temp < n) {
        temp += six_times;
        six_times += 6;
        cnt++;
    }
    if (n == 1) {
        printf("%d\n", 1);
    }
    else {
        printf("%d\n", cnt-1);
    }

    return 0;
}