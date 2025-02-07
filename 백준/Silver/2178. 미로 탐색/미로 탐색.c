#include <stdio.h>

int matrix[101][101];
int visited[101][101];

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

typedef struct {
    int x;
    int y;
} Queue;

Queue queue[10000];

void bfs() {
    int head = -1, rear = -1;
    int x = 0, y = 0;

    rear++;
    queue[rear].x = x;
    queue[rear].y = y;
    visited[x][y] = 1;

    while (head < rear) {
        head++;
        x = queue[head].x;
        y = queue[head].y;
        for (int i=0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (!visited[nx][ny] && matrix[nx][ny]) {
                visited[nx][ny] = visited[x][y] + 1;
                rear++;
                queue[rear].x = nx;
                queue[rear].y = ny;
            }
        }
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            scanf("%1d", &matrix[i][j]);
        }
    }

    bfs();

    printf("%d", visited[n-1][m-1]);
    return 0;
}