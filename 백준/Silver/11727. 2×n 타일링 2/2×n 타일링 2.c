#include <stdio.h>

int main(void) {
  int n;
  scanf("%d", &n);

  int dp[1001] = { 0, };
  dp[1] = 1;
  dp[2] = 3;

  if (n <= 2) {
    printf("%d", dp[n]);
  }
  else {
    for (int i=3; i < n+1; i++) {
      dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007;
    }
    printf("%d", dp[n] % 10007);
  }

  return 0;
}