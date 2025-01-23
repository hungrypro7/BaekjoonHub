#include <stdio.h>
#include <string.h>

int main(void) {

    do {
      
        char string[20] = {'\0'};
        gets(string);

        if (strcmp(string, "end") == 0) { break; }
        
        // 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        int is_gather = 0;
        for (int i=0; i < 20; i++) {
            if (string[i] == 'a' || string[i] == 'e' || string[i] == 'i' || string[i] == 'o' || string[i] == 'u') {
                is_gather = 1;
            }
        }

        // 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        int is_three = 1;
        for (int i=0 ; i < 18; i++) {
            int gather1 = 0;
            int gather2 = 0;
            for (int k = i; k < i + 3; k++) {

                if (string[k] == '\0') {
                    break;
                }

                if (string[k] == 'a') {
                    gather1++;
                }
                else if (string[k] == 'e') {
                    gather1++;
                }
                else if (string[k] == 'i') {
                    gather1++;
                }
                else if (string[k] == 'o') {
                    gather1++;
                }
                else if (string[k] == 'u') {
                    gather1++;
                }
                else {
                    gather2++;
                }
                
            }

            if (gather1 == 3 || gather2 == 3) {
                is_three = 0;
            }
        }
        
        // 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        int is_same = 1;
        for (int i=0; i < 20; i++) {
            if (string[i] != '\0' && (string[i] == string[i+1]) && (string[i] != 'e') && (string[i] != 'o')) {
                is_same = 0;
            }
        }

        if (is_gather && is_three && is_same) {
            printf("<%s> is acceptable.\n", string);
        }
        else {
            printf("<%s> is not acceptable.\n", string);
        }

    } while (1);

    return 0;
}