#include <stdio.h>

int main(void) {
	
	int n;
	scanf("%d", &n);

	int dp[50] = { 0, };
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 1;
	for (int i=3; i < n+1; i++) {
		dp[i] = dp[i-1] + dp[i-2];
	}

	printf("%d", dp[n]);
	return 0;
}