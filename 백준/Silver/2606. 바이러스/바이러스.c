#include <stdio.h>

int graph[101][101];
int visited[101];
int ans = 0;
int queue[101];

void bfs(int n) {
    int front = 0;
    int rear = 1;
    int pop;
    visited[1] = 1;
    queue[1] = 1;
    while (front < rear) {
        front++;
        pop = queue[front];
        for (int i=2; i <= n; i++) {
            if (graph[pop][i] && !visited[i]) {
                visited[i] = 1;
                ans++;
                rear++;
                queue[rear] = i;
            }
        }
    }
}

int main(void) {

    int n;  // 컴퓨터 수
    scanf("%d", &n);

    int pairs;  // 쌍의 수
    scanf("%d", &pairs);
    
    for (int i=0; i < pairs; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    bfs(n);
    printf("%d", ans);
    return 0;
}