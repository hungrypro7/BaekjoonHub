#include <stdio.h>

long long game[101][101];
long long dp[101][101] = { 0, };

int main(void) {
	
	int n;
	scanf("%d", &n);

	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			scanf("%d", &game[i][j]);
		}
	}

	dp[0][0] = 1;
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			if (game[i][j] && dp[i][j]) {
				if (i + game[i][j] < n) {		// 밑으로
					dp[i+game[i][j]][j] += dp[i][j];
				}
				if (j + game[i][j] < n) {		// 오른쪽으로
					dp[i][j+game[i][j]] += dp[i][j];
				}
			}
		}
	}

	printf("%lld", dp[n-1][n-1]);
	return 0;
}