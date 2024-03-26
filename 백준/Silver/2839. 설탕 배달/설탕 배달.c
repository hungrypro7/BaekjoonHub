#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    
    int dp[n+1];
    dp[0] = 0;
    dp[1] = 10000;
    dp[2] = 10000;
    dp[3] = 1;
    dp[4] = 10000;
    dp[5] = 1;
  
    if(n <= 5) {
      if(dp[n] == 10000) printf("%d", -1);
      else printf("%d", dp[n]);
    }
    else {
      for(int i=6; i<n+1; i++){
        if(dp[i-3] + 1 < dp[i-5] + 1) dp[i] = dp[i-3] + 1;
        else dp[i] = dp[i-5] + 1;
      }
      if(dp[n] >= 10000) printf("%d", -1);
      else printf("%d", dp[n]);
    }
    return 0;
}