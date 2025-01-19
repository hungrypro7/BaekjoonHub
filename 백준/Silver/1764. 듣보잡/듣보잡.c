#include <stdio.h>
#include <string.h>

int compare(void* first, void* second)
{
	return strcmp(first, second);
}

typedef struct {
    char input[21];
} name;

typedef struct {
    char input[21];
} save;

name name1[1000000];
save name2[1000000];

int main() {
    int n, m;
    scanf("%d %d \n", &n, &m);
    for (int i=0; i < n + m; i++) {
        scanf("%s", name1[i].input);
    }

    qsort(name1, n+m, sizeof(name1[0]), compare);

    int cnt = 0;
    for(int i=0; i < n + m; i++) {
        if (strcmp(name1[i].input, name1[i+1].input) == 0) {
            strcpy(name2[cnt].input, name1[i].input);
            cnt++;
        }
    }

    printf("%d \n", cnt);
    for(int i=0; i < cnt; i++) {
        printf("%s\n", name2[i].input);
    }

    return 0;
}