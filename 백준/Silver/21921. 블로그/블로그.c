#include <stdio.h>

int main(void) {
    int n, x;
    scanf("%d %d", &n, &x);     // 전체, 기간

    int visitors[250001];
    for (int i=1; i < n+1; i++) {
        scanf("%d", &visitors[i]);
    }

    for (int i=2; i < n+1; i++) {
        visitors[i] += visitors[i-1];
    }

    int start = 0; 
    int end = start + x;
    int max_visitor = -1e07;
    int num_of_visitor = 0;
    for (int i=end; i < n+1; i++) {
        if (visitors[end] - visitors[start] > max_visitor) {
            max_visitor = visitors[end] - visitors[start];
            num_of_visitor = 0;
        }
        if (visitors[end] - visitors[start] == max_visitor) {
            num_of_visitor++;
        }
        start++;
        end++;
    }

    if (max_visitor == 0) {
        printf("SAD");
    } else {
        printf("%d\n%d", max_visitor, num_of_visitor);
    }
    
    return 0;
}