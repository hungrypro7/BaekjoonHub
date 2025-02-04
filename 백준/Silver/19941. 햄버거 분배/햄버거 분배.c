#include <stdio.h>
#include <string.h>

int main(void) {
    
    int n, k;   // 식탁의 길이, 햄버거 선택 거리
    scanf("%d %d\n", &n, &k);

    char table_info[20002];
    for (int i=0; i < n; i++) {
        scanf("%c", &table_info[i]);
    }

    int ans=0;
    for (int i=0; i < n; i++) {
        if (table_info[i] == 'P') {
            for (int j=i-k; j <= i+k; j++) {
                if (0 <= j && j < n && table_info[j] == 'H') {
                    table_info[j] = 'O';
                    ans++;
                    break;
                }
            }
        }
    }

    printf("%d\n", ans);

    return 0;
}