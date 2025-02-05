#include <stdio.h>
#include <string.h>

int main(void) {
    char s[501];
    scanf("%s", s);     // 문자열 입력 받기

    int num_of_zero = 0;
    int num_of_one = 0;
    for (int i=0; s[i] != '\0'; i++) {
        if (s[i] == '0') { num_of_zero++; }
        else if (s[i] == '1') { num_of_one++; }
    }

    int noz = num_of_zero / 2;
    int noo = num_of_one / 2;

    for (int i=strlen(s); i > -1; i--) {
        if (s[i] == '0' && noz) {
            s[i] = 'a';
            noz--;
        }
    }

    for (int i=0; i < strlen(s); i++) {
        if (s[i] == '1' && noo) {
            s[i] = 'a';
            noo--;
        }
    }

    for (int i=0; i < strlen(s); i++) {
        if (s[i] != 'a') {
            printf("%c", s[i]);
        }
    }

    return 0;
}