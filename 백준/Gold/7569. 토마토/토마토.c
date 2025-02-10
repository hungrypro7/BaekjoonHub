#include <stdio.h>

int tomato[101][101][101] = { 0, };
int visited[101][101][101] = { 0, };
int dx[6] = {-1, 1, 0, 0, 0, 0};
int dy[6] = {0, 0, -1, 1, 0, 0};
int dz[6] = {0, 0, 0, 0, -1, 1};
int ans = 0;
int m, n, h;	// 가로, 세로, 상자의 수

typedef struct {
	int x;
	int y;
	int z;
} Queue;

int front;
int rear;
Queue q[1000001];

void bfs() {
	
	while (front < rear) {
		front++;
		int tx = q[front].x;
		int ty = q[front].y;
		int tz = q[front].z;
		for (int i=0; i < 6; i++) {
			int nx = tx + dx[i];
			int ny = ty + dy[i];
			int nz = tz + dz[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m && 0 <= nz && nz < h && !visited[nx][ny][nz] && tomato[nx][ny][nz] == 0) {
				visited[nx][ny][nz] = visited[tx][ty][tz] + 1;
				tomato[nx][ny][nz] = 1;
				rear++;
				q[rear].x = nx;
				q[rear].y = ny;
				q[rear].z = nz;
			}
		}
	}

	return;
}

int main(void) {

	scanf("%d %d %d", &m, &n, &h);

	for (int i=0; i < h; i++) {
		for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				scanf("%d", &tomato[j][k][i]);
			}
		}
	}

	front = -1;
	rear = -1;

	for (int i=0; i < h; i++) {
		for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				if (tomato[j][k][i] == 1 && !visited[j][k][i]) {
					rear++;
					q[rear].x = j;
					q[rear].y = k;
					q[rear].z = i;
					visited[j][k][i] = 1;
				}
			}
		}
	}

	bfs();

	for (int i=0; i < h; i++) {
		for (int j=0; j < n; j++) {
			for (int k=0; k < m; k++) {
				if (!tomato[j][k][i] && !visited[j][k][i]) {
					ans = -1;
					printf("%d", ans);
					return 0;
				}
			}
		}
	}

	printf("%d", visited[q[rear].x][q[rear].y][q[rear].z] - 1);
	return 0;
}