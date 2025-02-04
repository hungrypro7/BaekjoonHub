#include <stdio.h>
#include <string.h>

int main(void) {
    char n[3001];
    fgets(n, sizeof(n), stdin);  // 개행 포함 입력
    n[strcspn(n, "\n")] = '\0';  // 개행 문자 제거

    int p = 0;
    int i = 1;
    
    while (p < strlen(n)) {  // Python과 동일한 조건
        char str_i[3001];
        sprintf(str_i, "%d", i);  // i를 문자열로 변환

        for (int j = 0; str_i[j] != '\0'; j++) {
            if (str_i[j] == n[p]) {
                p++;
            }
            if (p == strlen(n)) {  // 종료 조건
                printf("%d\n", i);
                return 0;
            }
        }
        i++;
    }

    return 0;
}
