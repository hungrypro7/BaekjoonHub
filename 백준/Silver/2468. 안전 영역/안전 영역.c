#include <stdio.h>

int rain[101][101];
int visited[101][101];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int max(int a, int b) {
	if (a > b) { return a; }
	else { return b; }
}

int dfs(int x, int y, int n) {
	
	visited[x][y] = 1;
	
	for (int j=0; j < 4; j++) {
		int nx = x + dx[j];
		int ny = y + dy[j];
		if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && rain[nx][ny] > 0) {
			dfs(nx, ny, n);
		}
	}

	return 0;
}

int main(void) {
	
	int n;
	scanf("%d", &n);
	int max_rain = 0;
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			scanf("%d", &rain[i][j]);
			if (rain[i][j] > max_rain) {
				max_rain = rain[i][j];
			}
		}
	}

	int ans = 0;
	for (int i=0; i < max_rain+1; i++) {
		
		int temp = 0;
		for (int p=0; p < n; p++) {
			for (int q=0; q < n; q++) {
				if (rain[p][q] <= i) {
					rain[p][q] = -1;
				}
			}
		}

		for (int p=0; p < 101; p++) {
			for (int q=0; q < 101; q++) {
				visited[p][q] = 0;
			}
		}

		for (int p=0; p < n; p++) {
			for (int q=0; q < n; q++) {
				if (rain[p][q] > 0 && !visited[p][q]) {
					dfs(p, q, n);
					temp++;
				}
			}
		}

		ans = max(ans, temp);
	}

	printf("%d", ans);
	return 0;
}