#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int pos;	// 현재 있는 층
	int pressed_num;	// 누른 버튼 수
} Queue;

Queue q[1000001];
int visited[1000001];

int main(void) {
	
	int f, s, g, u, d;		// 총 층수, 지금 있는 층, 이동하려는 층, U 버튼, D 버튼
	scanf("%d %d %d %d %d", &f, &s, &g, &u, &d);

	int front = 0, rear = 0;
	q[rear].pos = s;
	q[rear].pressed_num = 0;
	visited[s] = 1;
	int status = 0;

	while (q[front].pos != g) {

		if (q[front].pos + u <= f) {
			if (!visited[q[front].pos + u]) {
				rear++;
				q[rear].pos = q[front].pos + u;
				q[rear].pressed_num = q[front].pressed_num + 1;
				visited[q[front].pos + u] = 1;
			}
		}

		if (q[front].pos - d > 0) {
			if (!visited[q[front].pos - d]) {
				rear++;
				q[rear].pos = q[front].pos - d;
				q[rear].pressed_num = q[front].pressed_num + 1;
				visited[q[front].pos - d] = 1;
			}
		}

		front++;
		
		if (front > rear) {
			break;
		}
	}
	
	if (!visited[g]) {
		printf("use the stairs");	
	}
	else {
		printf("%d\n", q[front].pressed_num);
	}

	return 0;
}