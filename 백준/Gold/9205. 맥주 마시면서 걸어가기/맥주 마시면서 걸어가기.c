#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct {
   int x;
   int y;
} POS;

POS home;
POS fes;
POS store[101];
int visited[101];

int bfs(int n) {

    int front = -1, rear = 0;
    POS q[101];
    q[0].x = home.x;
    q[0].y = home.y;

    while (front < rear) {
        front++;
        int x = q[front].x;
        int y = q[front].y;

        if (abs(fes.x - x) + abs(fes.y - y) <= 1000) { return 1; }
        for (int i=0; i < n; i++) {
            if (visited[i] == 1) { continue; }
            if (abs(store[i].x - x) + abs(store[i].y - y) <= 1000) {
                visited[i] = 1;
                rear++;
                q[rear].x = store[i].x;
                q[rear].y = store[i].y;
            }
        }

    }

    return 0;
}

int main(void) {

   int t;      // 테스트 케이스
   scanf("%d", &t);

   for (int i=0; i < t; i++) {
      int n;      // 편의점 개수
      scanf("%d", &n);

      int x, y;
      scanf("%d %d", &x, &y);
      home.x = x;
      home.y = y;

      for (int j=0; j < n; j++) {
         scanf("%d %d", &x, &y);
         store[j].x = x;
         store[j].y = y;
      }

      scanf("%d %d", &x, &y);
      fes.x = x;
      fes.y = y;

      memset(visited, 0, sizeof(visited));
      int pos = bfs(n);

      if (pos) {
        printf("happy\n");
      }
      else {
        printf("sad\n");
      }

   }

   return 0;
}