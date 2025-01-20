#include <stdio.h>

int max(int a, int b, int c) {
    int temp = -1000;

    if (a > temp) {
        temp = a;
    }

    if (b > temp) {
        temp = b;
    }

    if (c > temp) {
        temp = c;
    }

    return temp;
}

int main() {

    int a, b, c;

    do {
        
        scanf("%d %d %d", &a, &b, &c);

        if (a == 0 && b == 0 && c == 0) {
            break;
        }

        int max_num = max(a, b, c);

        if (max_num >= (a + b + c - max_num)) {
            printf("Invalid\n");
        }
        else if (a == b && b == c && a == c) {
            printf("Equilateral\n");
        }
        else if (a != b && b != c && a != c) {
            printf("Scalene\n");
        }
        else {
            printf("Isosceles\n");
        }

    } while (1);

    return 0;
}