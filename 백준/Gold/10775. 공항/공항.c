#include <stdio.h>
#include <stdlib.h>

int parents[100001];

int findparent(int x) {
	if (parents[x] == x) {
		return x;
	}

	return parents[x] = findparent(parents[x]);
}

void unionsets(int a, int b) {
	int parentx = findparent(a);
	int parenty = findparent(b);

	if (parentx != parenty) {
		parents[parentx] = parenty;
	}
}

int main(void) {
	
	int g;		// 게이트 수
	scanf("%d", &g);

	int p;		// 비행기 수
	scanf("%d", &p);

	for (int i=0; i < 100001; i++) {
		parents[i] = i;
	}

	int temp[100001] = { 0, };
	for (int i=0; i < p; i++) {
		scanf("%d", &temp[i]);
	}

	int input;
	int cnt = 0;
	for (int i=0; i < p; i++) {

		input = temp[i];
		int prev = findparent(input);

		if (prev == 0) {
			break;
		}
		else {
			unionsets(prev, prev-1);
			cnt++;
		}
	}

	printf("%d\n", cnt);
	return 0;
}