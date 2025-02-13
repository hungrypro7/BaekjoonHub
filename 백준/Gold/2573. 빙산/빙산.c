#include <stdio.h>
#include <memory.h>

int ice[301][301];
int save[301][301];
int visited[301][301];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y, int n, int m) {

	visited[x][y] = 1;

	for (int i=0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && ice[nx][ny] > 0) {
			dfs(nx, ny, n, m);
		}
	}

	return 0;
}

int max(int a, int b) {
	if (a > b) { return a; }
	else { return b; }
}

int main(void) {
	
	int n, m;	// 행, 열
	scanf("%d %d", &n, &m);
	
	for (int i=0; i < n; i++) {
		for (int j=0; j < m; j++) {
			scanf("%d", &ice[i][j]);
		}
	}

	int cnt = 0;
	int ans_time = 0;
	while (cnt < 2) {

		cnt = 0;

		memset(visited, 0, sizeof(visited));

		for (int i=0; i < n; i++) {
			for (int j=0; j < m; j++) {
				if (ice[i][j] > 0 && !visited[i][j]) {
					dfs(i, j, n, m);
					cnt++;
				}
			} 
		}

		if (ans_time == 0 && cnt >= 2) {
			printf("0");
			return 0;
		}

		memset(save, 0, sizeof(save));

		for (int i=0; i < n; i++) {
			for (int j=0; j < m; j++) {
				if (ice[i][j] > 0) {
					int temp = 0;
					for (int k=0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (0 <= nx && nx < n && 0 <= ny && ny < m && !ice[nx][ny]) {
							temp++;
						}
					}
					save[i][j] = temp;
				}
			}
		}

		int num_of_0 = 0;
		for (int i=0; i < n; i++) {
			for (int j=0; j < m; j++) {
				if (ice[i][j] > 0) {
					ice[i][j] = max(0, ice[i][j] - save[i][j]);
					num_of_0++;
				}
			}
		}

		if (num_of_0 == 0) {
			printf("0");
			return 0;
		}

		ans_time++;
	}

	printf("%d", ans_time-1);
	return 0;
}