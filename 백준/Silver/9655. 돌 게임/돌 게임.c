#include <stdio.h>
#include <string.h>

int main(void) {
    
    int n;
    int dp[1001] = { 0 };
    scanf("%d", &n);

    for (int i = 1; i < 1000; i++) {
        if (dp[i-1] + 3 > n) {
            dp[i] = dp[i-1] + 1;
        }
        else {
            dp[i] = dp[i-1] + 3;
        }

        if (dp[i] == n) {
            if (i % 2 == 0) {
                printf("CY\n");
            }
            else {
                printf("SK\n");
            }
            break;
        }
    }

    return 0;
}