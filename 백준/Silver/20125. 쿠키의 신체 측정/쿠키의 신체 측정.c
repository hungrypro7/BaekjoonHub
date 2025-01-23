#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {

    int n;
    scanf("%d\n", &n);

    char **arr = (char**) malloc(sizeof(char*) * n);
    for(int i=0; i < n; i++){
        arr[i] = (char*) malloc (sizeof(char) * n);
    }

    for (int i=0; i < n; i++) {
        for (int j=0; j < n; j++) {
            scanf("%c", &arr[i][j]);
        }
        getchar();      // 각 줄의 개행 문자 (\n) 처리
    }

    int h_x = 0;    // 심장의 위치
    int h_y = 0;
    int left_a = 0;     // 왼쪽 팔
    int right_a = 0;    // 오른쪽 팔
    int center = 0;     // 허리
    int left_l = 0;     // 왼쪽 다리
    int right_l = 0;    // 오른쪽 다리
    
    // 심장 위치
    int status = 0;
    for (int i = 0; i < n; i++) {
        for (int j=0; j < n; j++) {
            if (arr[i][j] == '*') {
                h_x = i + 2;
                h_y = j + 1;
                status = 1;
                break;
            }
        }
        if (status) {
            break;
        }
    }

    // 왼쪽 팔, 오른쪽 팔
    int arm_s = 0;
    int arm_e = 0;
    for (int i = 0; i < n; i++) {
        if (arr[h_x - 1][i] == '*') {
            arm_s = i + 1;
            break;
        }
    }
    for (int i = n; i > -1; i--) {
        if (arr[h_x - 1][i] == '*') {
            arm_e = i + 1;
            break;
        }
    }
    left_a = h_y - arm_s;
    right_a = arm_e - h_y;

    // 허리
    int cnt;
    for (int i = h_x; i < n; i++) {
        cnt = 0;
        for (int j = 0; j < n; j++) {
            if (arr[i][j] == '*') {
                cnt++;
            }
        }
        if (cnt == 1) {
            center++;
            continue;
        }
        else {
            break;
        }
    }

    // 왼쪽 다리, 오른쪽 다리
    int left_idx = 0;
    int right_idx = 0;
    for (int i = 0; i < n; i++) {
        if (arr[h_x + center][i] == '*') {
            left_idx = i;
            left_l++;
            break;
        }
    }

    for (int i= n-1; i > -1; i--) {
        if (arr[h_x + center][i] == '*') {
            right_idx = i;
            right_l++;
            break;
        }
    }

    for (int i=h_x + center + 1; i < n; i++) {
        if (arr[i][left_idx] == '*') {
            left_l++;
        }
        if (arr[i][right_idx] == '*') {
            right_l++;
        }
    }

    printf("%d %d\n", h_x, h_y);
    printf("%d %d %d %d %d", left_a, right_a, center, left_l, right_l);

    for (int i=0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}