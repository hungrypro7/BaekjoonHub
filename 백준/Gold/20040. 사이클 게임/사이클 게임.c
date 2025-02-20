#include <stdio.h>

int parents[500001];

int findparent(int x) {
	if (parents[x] == x) {
		return x;
	}
	else {
		return parents[x] = findparent(parents[x]);
	}
}

int unionsets(int a, int b) {
	int parentx = findparent(a);
	int parenty = findparent(b);

	if (parentx == parenty) {
		return 1;
	}
	else {
		parents[parentx] = parenty;
		return 0;
	}
}

typedef struct {
	int x;
	int y;
} B;

B temp[1000001]; 

int main(void) {
	
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i=0; i < n; i++) {
		parents[i] = i;
	}

	int x, y;
	for (int i=0; i < m; i++) {
		scanf("%d %d", &x, &y);
		temp[i].x = x;
		temp[i].y = y;
	}

	int cnt = 1;
	for (int i=0; i < m; i++) {
		x = temp[i].x;
		y = temp[i].y;
		int prev = unionsets(x, y);

		if (prev) {
			break;
		}
		else {
			cnt++;
		}
	}

	if (cnt != m+1) {
		printf("%d\n", cnt);
	}
	else {
		printf("%d\n", 0);
	}

	return 0;
}