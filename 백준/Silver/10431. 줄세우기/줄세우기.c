#include <stdio.h>

int main(void) {
    
    int p;
    scanf("%d", &p);

    for (int i = 0; i < p; i++) {
        int num;
        scanf("%d", &num);

        int cnt = 0;
        int heights[20] = { 0 };

        for (int j = 0; j < 20; j++) {
            int temp;
            scanf("%d", &temp);
            
            heights[j] = temp;
            for (int k = 0; k < j; k++) {

                if (heights[k] > heights[j]) {
                    for (int l = j - 1; l >= k; l--) {
                        heights[l + 1] = heights[l];
                        cnt++;
                    }
                    heights[k] = temp;
                    break;
                }
            }
        }

        printf("%d %d\n", num, cnt);
    }

    return 0;
}