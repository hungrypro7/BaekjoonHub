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

void unionsets(int a, int b) {
	int parentx = findparent(a);
	int parenty = findparent(b);

	if (parentx < parenty) {
		parents[parentx] = parenty;
	}
	else {
		parents[parenty] = parentx;
	}
}

int main(void) {
	
	int n;		// 도시의 수
	scanf("%d", &n);

	parents = malloc(sizeof(int) * n);
	for (int i=0; i < n; i++) {
		parents[i] = i;
	}

	int m;		// 여행 계획에 속한 도시의 수
	scanf("%d", &m);

	int input;
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			scanf("%d", &input);

			if (input == 1) {
				unionsets(i, j);
			}
		}
	}

	int is_possible = 1;
	scanf("%d", &input);
	int prevparent = findparent(input - 1);
	for (int i=1; i < m; i++) {
		scanf("%d", &input);

		if (findparent(input - 1) != prevparent) {
			is_possible = 0;
			break;
		}
	}

	if (is_possible) {
		printf("YES\n");
	} 
	else {
		printf("NO\n");
	}

	free(parents);

	return 0;
}