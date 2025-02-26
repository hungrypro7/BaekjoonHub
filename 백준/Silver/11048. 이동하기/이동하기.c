#include <stdio.h>

int miro[1000][1000];
int dp[1000][1000];

int max(int a, int b) {
	if (a > b) { return a; }
	else { return b; }
}

int main(void) {
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i=0; i < n; i++) {
		for (int j=0; j < m; j++) {
			scanf("%d", &miro[i][j]);
		}
	}

	for (int i=0; i < n; i++) {
		for (int j=0; j < m; j++) {
			if (i == 0 && j == 0) {
				dp[i][j] = miro[0][0];
			}
			else if (j == 0) {
				dp[i][j] = dp[i-1][j] + miro[i][j];
			}
			else if (i == 0) {
				dp[i][j] = dp[i][j-1] + miro[i][j];
			}
			else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + miro[i][j];
			}	
		}
	}

	printf("%d", dp[n-1][m-1]);
	return 0;
}