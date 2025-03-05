#include <stdio.h>

int min(int a, int b) {
  if (a > b) { return b; }
  else { return a; }
}

int min3(int a, int b, int c) {
  int tmp = 1e07;
  if (tmp > a) { tmp = a; }
  if (tmp > b) { tmp = b; }
  if (tmp > c) { tmp = c; }
  return tmp;
}

int main(void) {

  int t;
  scanf("%d", &t);

  int d1, m1, m3, y1;
  for (int i=0; i < t; i++) {

    int dp[13] = { 0, };
    int month[13];
    int ans;
    scanf("%d %d %d %d", &d1, &m1, &m3, &y1);
    for (int j=1; j < 13; j++) {
      scanf("%d", &month[j]);
    }

    dp[1] = min(month[1] * d1, m1);
    for (int j=2; j < 13; j++) {
      if (j > 2) {
        dp[j] = min3(dp[j-1] + d1 * month[j], dp[j-1] + m1, dp[j-3] + m3);
      }
      else {
        dp[j] = min(dp[j-1] + month[j] * d1, dp[j-1] + m1);
      }
    }

    ans = min(dp[12], y1);

    printf("#%d %d\n", i+1, ans);

  }
  return 0;
}