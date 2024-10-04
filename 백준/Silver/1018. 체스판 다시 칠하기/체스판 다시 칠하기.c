#include <stdio.h>
#include <stdlib.h>

#define MAX_N 50
#define MAX_M 50

char chess[MAX_N][MAX_M];

// WBWBWBWB로 시작하는 경우의 비교 함수
int compare1(char temp[8][8]) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (i % 2 == 0) {
                if (j % 2 == 0 && temp[i][j] != 'W') {
                    count++;
                } else if (j % 2 == 1 && temp[i][j] != 'B') {
                    count++;
                }
            } else {
                if (j % 2 == 1 && temp[i][j] != 'W') {
                    count++;
                } else if (j % 2 == 0 && temp[i][j] != 'B') {
                    count++;
                }
            }
        }
    }
    return count;
}

// BWBWBWBW로 시작하는 경우의 비교 함수
int compare2(char temp[8][8]) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (i % 2 == 0) {
                if (j % 2 == 0 && temp[i][j] != 'B') {
                    count++;
                } else if (j % 2 == 1 && temp[i][j] != 'W') {
                    count++;
                }
            } else {
                if (j % 2 == 1 && temp[i][j] != 'B') {
                    count++;
                } else if (j % 2 == 0 && temp[i][j] != 'W') {
                    count++;
                }
            }
        }
    }
    return count;
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    // 체스판 입력 받기
    for (int i = 0; i < n; i++) {
        scanf("%s", chess[i]);
    }

    int answer = 64;  // 최악의 경우 (8x8 전체가 다 바뀌는 경우)

    // 8x8 크기로 자를 수 있는 모든 경우를 탐색
    for (int i = 0; i <= n - 8; i++) {
        for (int j = 0; j <= m - 8; j++) {
            char temp[8][8];

            // 8x8 크기로 자른 체스판 만들기
            for (int k = 0; k < 8; k++) {
                for (int l = 0; l < 8; l++) {
                    temp[k][l] = chess[i + k][j + l];
                }
            }

            // 두 가지 패턴을 비교하고 작은 값을 선택
            int a = compare1(temp);
            int b = compare2(temp);
            int min_val = a < b ? a : b;

            // 최소값을 갱신
            if (min_val < answer) {
                answer = min_val;
            }
        }
    }

    printf("%d\n", answer);

    return 0;
}

