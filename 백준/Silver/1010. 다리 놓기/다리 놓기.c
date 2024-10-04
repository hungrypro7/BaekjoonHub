#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);
    
    
    for (int i=0; i<t; i++) {
        int s, e;
        scanf("%d %d", &s, &e);
        
        int po = 1;
        int dp[50];
        dp[0] = e;
        
        int c;
        for (int j=1; j<s; j++) {
            c = (dp[po-1] * (e-j)) / (j+1);
            dp[po] = c;
            po++;
        }
        printf("%d\n", dp[s-1]);
    }
}
