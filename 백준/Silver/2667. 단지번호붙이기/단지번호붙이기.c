#include <stdio.h>
#include <stdlib.h>

int matrix[26][26];
int visited[26][26];
int home_size[800];
int ans;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

typedef struct {
    int x;
    int y;
} Queue;

int compare(const void* a, const void *b) {
    return (*(int*)a - *(int*)b);
}

void bfs(int x, int y, int n) {
    int temp_size = 1;
    int front = 0, rear = 1;
    int pop_x;
    int pop_y;
    Queue queue[1000];
    visited[x][y] = 1;
    queue[0].x = x;
    queue[0].y = y;
    while (front < rear) {
        pop_x = queue[front].x;
        pop_y = queue[front].y;
        front++;
        for (int i=0; i < 4; i++) {
            int nx = pop_x + dx[i];
            int ny = pop_y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && matrix[nx][ny] && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                temp_size++;
                queue[rear].x = nx;
                queue[rear].y = ny;
                rear++;
            }
        }
    }
    home_size[ans] = temp_size;
}

int main(void) {
    int n;    // 지도의 크기
    scanf("%d", &n);

    for (int i=0; i < n; i++) {
        for (int j=0; j < n; j++) {
            scanf("%1d", &matrix[i][j]);
        }
    }

    ans = 0;
    for (int i=0; i < n; i++) {
        for (int j=0; j < n; j++) {
            if (matrix[i][j] && !visited[i][j]) {
                bfs(i, j, n);
                ans++;
            }
        }
    }

    printf("%d\n", ans);
    qsort(home_size, ans, sizeof(home_size[0]), compare);
    for (int i=0; i < ans; i++) {
        printf("%d\n", home_size[i]);
    }

    return 0;
}