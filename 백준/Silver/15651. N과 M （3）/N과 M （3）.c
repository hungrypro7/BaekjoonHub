#include <stdio.h>

int n, m;
int arr[7];

void back(int cnt) {
	if (cnt == m) {
		for (int i=0; i < m; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
	}
	else {
		for (int i=1; i <= n; i++) {
			arr[cnt] = i;
			back(cnt + 1);
		}
	}
}

int main(void) {

	scanf("%d %d", &n, &m);

	back(0);

	return 0;
}