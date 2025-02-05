#include <stdio.h>
#include <stdlib.h>

int min(int a, int b) {
    if (a > b) { return b; }
    else { return a; }
}

int main(void) {
    int n, m;       // 행, 열
    scanf("%d %d", &n, &m);

    int **arr = (int **)malloc(n * sizeof(int *));      // 행
    for (int i=0; i < n; i++) {         // 열
        arr[i] = (int *)malloc(m * sizeof(int));
    }

    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    int ***dp = (int ***)malloc(n * sizeof(int **));      // 행
    for (int i=0; i < n; i++) {         // 열
        dp[i] = (int **)malloc(m * sizeof(int *));

        for (int j=0; j < m; j++) {
            dp[i][j] = (int *)malloc(3 * sizeof(int));
        }
    }

    for (int i=0; i<m; i++) {
        for (int j=0; j < 3; j++) {
            dp[0][i][j] = arr[0][i];
        }
    }

    for (int i=1; i < n; i++) {
        for (int j=0; j < m; j++) {
            for (int k=0; k < 3; k++) {
                if ((j == 0 && k == 0) || (j == m-1 && k == 2)) {
                    dp[i][j][k] = 1e06;
                }
                else if (k == 0) {
                    dp[i][j][0] = arr[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2]);
                }
                else if (k == 1) {
                    dp[i][j][1] = arr[i][j] + min(dp[i-1][j][0], dp[i-1][j][2]);
                }
                else if (k == 2) {
                    dp[i][j][2] = arr[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1]);
                }
            }
        }
    }

    int result = 1e06;
    for (int i=0; i < m; i++) {
        for (int j=0; j < 3; j++) {
            result = min(result, dp[n-1][i][j]);
        }
    }

    printf("%d", result);

    return 0;
}