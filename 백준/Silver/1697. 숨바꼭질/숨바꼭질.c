#include <stdio.h>

typedef struct {
	int pos;
	int num;
} LOC;

LOC q[100001];
int visited[100001];

int main(void) {
	
	int n, k;
	scanf("%d %d", &n, &k);

	int front = 0, rear = 0;
	q[front].pos = n;
	q[front].num = 0;
	visited[n] = 1;

	while (q[front].pos != k) {

		if (q[front].pos > 0) {
			int new = q[front].pos - 1;
			if (!visited[new]) {
				rear++;
				q[rear].pos = new;
				q[rear].num = q[front].num + 1;
				visited[new] = 1;
			}
		}

		if (q[front].pos < k) {
			int new = q[front].pos + 1;
			if (!visited[new]) {
				rear++;
				q[rear].pos = new;
				q[rear].num = q[front].num + 1;
				visited[new] = 1;
			}
		}

		if (2 * q[front].pos <= k+1) {
			int new = q[front].pos * 2;
			if (!visited[new]) {
				rear++;
				q[rear].pos = new;
				q[rear].num = q[front].num + 1;
				visited[new] = 1;
			}
		}
		front++;
	}
	
	printf("%d", q[front].num);
	return 0;
}