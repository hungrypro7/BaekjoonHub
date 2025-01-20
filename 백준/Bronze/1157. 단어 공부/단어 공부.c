#include <stdio.h>

int main(void) {
    
    char word[1000001];
    int alphabet[26] = { 0 };

    scanf("%s", word);

    int temp = 0;       // 최대 알파벳 개수
    int indx = 0;       // 최대 알파벳 위치

    // A : 65, a : 97
    for (int i=0; i < 1000001; i++) {
        int ascii = word[i];

        if (word[i] == '\0') { break; }

        if (ascii < 97) {
            ascii += 32;
        }
        alphabet[ascii - 97] += 1;

        if (alphabet[ascii - 97] > temp) {
            temp = alphabet[ascii - 97];
            indx = ascii - 97;
        }
    }

    int cnt = 0;
    for (int i = 0; i < 26; i++) {
        if (alphabet[i] == temp) {
            cnt++;
        }
    }

    if (cnt > 1) {
        printf("?");
    }
    else {
        printf("%c", indx + 65);
    }

    return 0;
}