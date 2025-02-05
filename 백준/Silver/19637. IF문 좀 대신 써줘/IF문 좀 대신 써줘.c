#include <stdio.h>

typedef struct {
    char st[12];
    int max_skill;
} combat;

int main(void) {
    int n, m;       // 칭호, 캐릭터 개수
    scanf("%d %d", &n, &m);

    combat cb[n];
    for (int i=0; i < n; i++) {
        scanf("%s %d", cb[i].st, &cb[i].max_skill);
    }

    for (int i=0; i < m; i++) {
        int each_combat;
        scanf("%d", &each_combat);
        int start = 0;
        int end = n;
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (cb[mid].max_skill >= each_combat) {
                end = mid - 1;
            }   
            else {
                start = mid + 1;
            }
        }
        printf("%s\n", cb[start].st);
    }

    return 0;
}