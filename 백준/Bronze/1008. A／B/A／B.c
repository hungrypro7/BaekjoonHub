#include <stdio.h>

int main() {
    int A, B;

    // 두 정수 A와 B 입력받기
    scanf("%d %d", &A, &B);

    // A / B 결과를 소수점 아래 9자리까지 출력
    printf("%.9f\n", (double)A / B);

    return 0;
}
