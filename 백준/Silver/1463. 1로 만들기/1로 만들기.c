#include <stdio.h>

int min3(int a, int b, int c) {
	int temp = 1e07;
	if (a < temp) {
		temp = a;
	}
	if (b < temp) {
		temp = b;
	}
	if (c < temp) {
		temp = c;
	}
	return temp;
}

int min2(int a, int b) {
	if (a > b) { return b; }
	else { return a; }
}

int main(void) {

	int n;
	scanf("%d", &n);

	int dp[1000001] = { 0, };
	dp[2] = 1;
	dp[3] = 1;
	int po = 3;

	if (n <= 3) {
		printf("%d", dp[n]);
	}
	else {
		for (int i=4; i < n+1; i++) {
			if (i % 6 == 0) {
				po++;
				dp[po] = min3(dp[(int)(i/3)] + 1, dp[(int)(i/2)] + 1, dp[i-1] + 1);
			}
			else if (i % 3 == 0) {
				po++;
				dp[po] = min2(dp[(int)(i/3)] + 1, dp[i-1] + 1);
			}
			else if (i % 2 == 0) {
				po++;
				dp[po] = min2(dp[(int)(i/2)] + 1, dp[i-1] + 1);
			}
			else {
				po++;
				dp[po] = dp[i-1] + 1;
			}
		}
		printf("%d", dp[n]);
	}
	
	return 0;
}