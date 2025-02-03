#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[21];
    int count;      // 등장 횟수
    int len;    // 단어 길이
} Namelist;

int compare1(const void *a, const void *b) {
    Namelist A = *(Namelist *)a, B = *(Namelist *)b;
    if (strcmp(A.name, B.name) > 0) { return 1; }       // A.name이 B.name 보다 사전순으로 뒤에 있음
    else { return -1; }         // A.name이 B.name 보다 사전순으로 앞에 있음
}

int compare2(const void *a, const void *b) {
    Namelist A = *(Namelist *)a, B = *(Namelist *)b;
    if (A.count < B.count) { return 1; }
    else if (A.count == B.count) {
        if (A.len < B.len) { return 1; }
        else if (A.len == B.len) {
            if (strcmp(A.name, B.name) > 0) { return 1; }
            else { return -1; }
        }
        else { return -1; }
    }
    else { return -1; }
}

int main(void) {
    int n, m;       // 단어의 개수, 길이 기준
    scanf("%d %d", &n, &m);

    char word[11];
    int wordlen;
    Namelist namelist[n];
    int wi = 0;

    for (int i=0; i < n; i++) {
        scanf("%s", word);
        wordlen = strlen(word);
        if (wordlen >= m) {
            strcpy(namelist[wi].name, word);
            namelist[wi].len = wordlen;
            wi++;
        }
    }
    qsort(namelist, wi, sizeof(Namelist), compare1);    // 사전순으로 정렬

    Namelist printname[wi];

    strcpy(printname[0].name, namelist[0].name);
    printname[0].len = namelist[0].len;
    printname[0].count = 1;

    int co = 0;
    for (int i=1; i < wi; i++) {
        if (strcmp(namelist[i].name, namelist[i-1].name) == 0) {        // 같은 단어가 중복되면
            printname[co].count++;
        }
        else {      // 다른 단어가 나오면
            co++;
            strcpy(printname[co].name, namelist[i].name);
            printname[co].len = namelist[i].len;
            printname[co].count = 1;
        }
    }
    qsort(printname, co+1, sizeof(Namelist), compare2);

    for (int i=0; i < co+1; i++) {
        printf("%s\n", printname[i].name);
    }

    return 0;
}