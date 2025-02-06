#include <stdio.h>
#include <string.h>

typedef struct {
    int level;
    char nic[16];
} member;   // 방 내 회원

typedef struct {
    member m[301];
    int mem;
} room;     // 방

int compare(const void *a, const void *b) {
    return strcmp(((member *)a)->nic, ((member *)b)->nic);
}

int main(void) {
    int p, m;   // 플레이어 수, 방의 정원
    room r[301];
    scanf("%d %d", &p, &m);

    int num_of_room = 0;
    int l;
    char n[16];
    scanf("%d %s", &l, n);    // 레벨, 닉네임
    r[0].mem = 1;
    r[0].m[r[0].mem-1].level = l;
    strcpy(r[0].m[r[0].mem-1].nic, n);
    num_of_room++;

    for (int i=1; i < p; i++) {
        scanf("%d %s", &l, n);
        int state = 0;
        for (int j=0; j < num_of_room; j++) {
            if (r[j].mem < m && r[j].m[0].level - 10 <= l && l <= r[j].m[0].level + 10) {
                r[j].mem++;
                r[j].m[r[j].mem-1].level = l;
                strcpy(r[j].m[r[j].mem-1].nic, n);
                state = 1;
                break;
            }
        }
        if (!state) {        // 방에 들어가지 못했다면 새로운 방 만들기
            r[num_of_room].mem = 1;
            r[num_of_room].m[r[num_of_room].mem-1].level = l;
            strcpy(r[num_of_room].m[r[num_of_room].mem-1].nic, n);
            num_of_room++;
        }
    }

    for (int i=0; i < num_of_room; i++) {
        if (r[i].mem == m) {
            printf("Started!\n");
        }
        else {
            printf("Waiting!\n");
        }
        qsort(r[i].m, r[i].mem, sizeof(member), compare);
        for (int j=0; j < r[i].mem; j++) {
            printf("%d %s\n", r[i].m[j].level, r[i].m[j].nic);
        }
    }

    return 0;
}