#include <stdio.h>

#define MAX 51

int cabbage[MAX][MAX];
int count = 0;
int n, m;

void dfs(int a, int b) {
    cabbage[a][b] = 0;
    if (0 <= a-1 <= n-1 && cabbage[a-1][b] == 1) {
        dfs(a-1, b);
    }
    if (0 <= a+1 <= n-1 && cabbage[a+1][b] == 1) {
        dfs(a+1, b);
    }
    if (0 <= b-1 <= m-1 && cabbage[a][b-1] == 1) {
        dfs(a, b-1);
    }
    if (0 <= b+1 <= m-1 && cabbage[a][b+1] == 1) {
        dfs(a, b+1);
    }
}

int main(void) {
    int t;
    scanf("%d", &t);    // 테스트 케이스 개수
    
    int ans[100];
    int po = 0;
    for(int i=0; i<t; i++) {
        int k;
        scanf("%d %d %d", &m, &n, &k);
        
        for(int j=0; j<MAX; j++) {    // cabbage 초기화
            for(int k=0; k<MAX; k++) {
                cabbage[j][k] = 0;
            }
        }
        
        for(int j=0; j<k; j++) {
            int x, y;
            scanf("%d %d", &x, &y);
            cabbage[y][x] = 1;
        }
        count = 0;

        for(int p=0; p<n; p++) {
            for(int q=0; q<m; q++) {
                if (cabbage[p][q] == 1) {
                    dfs(p, q);
                    count++;
                }
            }
        }
        ans[po] = count;
        po++;
    }
    
    for (int i=0; i<po; i++) {
        printf("%d\n", ans[i]);
    }
    
    return 0;
}
