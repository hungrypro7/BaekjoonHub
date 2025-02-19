#include <stdio.h>
#include <stdlib.h>

int *parents;

int findparent(int x) {
	if (parents[x] == x) {
		return x;
	}

	parents[x] = findparent(parents[x]);
	return parents[x];
}

void unionsets(int x, int y) {
	int parentx = findparent(x);
	int parenty = findparent(y);

	if (parentx < parenty) {
		parents[parentx] = parenty;
	}
	else {
		parents[parenty] = parentx;
	}
}

int main(void) {

	int n, m;	// 집합 수, 연산 개수
	scanf("%d %d", &n, &m);

	parents = malloc(sizeof(int) * (n+1));

	for (int i=1; i < n+1; i++) {
		parents[i] = i;
	}

	int order, a, b;
	int parent_a, parent_b;
	for (int i=0; i < m; i++) {

		scanf("%d %d %d", &order, &a, &b);

		if (order == 0) {
			unionsets(a, b);
		}
		else {
			parent_a = findparent(a);
			parent_b = findparent(b);

			if (parent_a == parent_b) {
				printf("YES\n");
			}
			else {
				printf("NO\n");
			}
		}
	}

	return 0;
}