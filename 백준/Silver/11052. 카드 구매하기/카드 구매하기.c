#include <stdio.h>

int dp[1001] = { 0, };
int card[1001];

int max(int a, int b) {
	if (a > b) { return a; }
	else { return b; }
}

int main(void) {
	int n;
	scanf("%d", &n);
	
	for (int i=1; i < n+1; i++) {
		scanf("%d", &card[i]);
	}

	for (int i=1; i < n+1; i++) {
		for (int j=1; j <= i; j++) {
			dp[i] = max(dp[i], dp[i-j] + card[j]);
		}
	}

	printf("%d", dp[n]);
	return 0;
}