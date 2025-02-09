#include <stdio.h>

int rel[101][101];
int visited[101];
int ans = -1;

void dfs(start, end, cnt) {
	
	visited[start] = 1;

	if (start == end) {
		ans = cnt;
		return;
	}

	for (int i=0; i < 101; i++) {
		if (rel[start][i] && !visited[i]) {
			dfs(i, end, cnt+1);
		}
	}
}

int main(void) {
	
	int n;    // 전체 사람의 수
	scanf("%d", &n);

	int c1, c2;		// 촌수를 계산해야 하는 번호
	scanf("%d %d", &c1, &c2);

	int m;		// 부모 자식들 간의 관계 수
	scanf("%d", &m);

	for (int i=0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		rel[x][y] = 1;
		rel[y][x] = 1;
	}

	dfs(c1, c2, 0);
	printf("%d\n", ans);

	return 0;
}