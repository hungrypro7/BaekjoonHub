#include <stdio.h>

int visited[1001] = { 0, };
int graph[1001][1001] = { 0, };
int queue[1001];

void dfs(int v, int n) {
    visited[v] = 1;
    printf("%d ", v);
    for (int i=1; i <= n; i++) {
        if (graph[v][i] && !visited[i]) {
            dfs(i, n);
        }
    }
}

void bfs(int v, int n) {
    int front = 0;
    int rear = 1;
    int pop;

    visited[v] = 1;
    printf("%d ", v);
    queue[0] = v;
    while (front < rear) {
        pop = queue[front++];
        for (int i=1; i <= n; i++) {
            if (graph[pop][i] && !visited[i]) {
                visited[i] = 1;
                printf("%d ", i);
                queue[rear++] = i;
            }
        }
    }
}

int main(void) {
    int n, m, v;    // 정점 개수, 간선 개수, 정점 번호 (탐색 시작)
    scanf("%d %d %d", &n, &m, &v);

    for (int i=0; i < m; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    visited[v] = 1;
    dfs(v, n);

    for (int i=1; i <= n; i++) {
        visited[i] = 0;
    }
    visited[v] = 1;
    printf("\n");
    bfs(v, n);

    return 0;
}