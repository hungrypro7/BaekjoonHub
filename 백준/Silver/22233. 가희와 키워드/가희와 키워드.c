#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NUM_OF_KEYWORD 200001
#define LENGTH_OF_KEYWORD 11
#define HASH_SIZE 400009  // NUM_OF_KEYWORD의 약 2배인 소수로 변경

typedef struct Node {
    char keyword[LENGTH_OF_KEYWORD];
    struct Node* next;
} Node;

typedef struct {
    Node* table[HASH_SIZE];
} HashTable;

// 해시 함수
unsigned int hash(const char* str) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % HASH_SIZE;
}

// 해시 테이블 초기화
void initHashTable(HashTable* ht) {
    memset(ht->table, 0, sizeof(Node*) * HASH_SIZE);
}

// 키워드 삽입
void insert(HashTable* ht, const char* keyword) {
    unsigned int h = hash(keyword);
    
    Node* newNode = (Node*)malloc(sizeof(Node));
    strcpy(newNode->keyword, keyword);
    newNode->next = ht->table[h];
    ht->table[h] = newNode;
}

// 키워드 검색 및 삭제
int searchAndRemove(HashTable* ht, const char* keyword) {
    unsigned int h = hash(keyword);
    Node* current = ht->table[h];
    Node* prev = NULL;

    while (current != NULL) {
        if (strcmp(current->keyword, keyword) == 0) {
            if (prev == NULL) {
                ht->table[h] = current->next;
            } else {
                prev->next = current->next;
            }
            free(current);
            return 1;
        }
        prev = current;
        current = current->next;
    }
    return 0;
}

// 해시 테이블 메모리 해제
void freeHashTable(HashTable* ht) {
    for (int i = 0; i < HASH_SIZE; i++) {
        Node* current = ht->table[i];
        while (current != NULL) {
            Node* next = current->next;
            free(current);
            current = next;
        }
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    HashTable ht;
    initHashTable(&ht);

    // 키워드 입력 및 해시 테이블에 저장
    for (int i = 0; i < n; i++) {
        char keyword[LENGTH_OF_KEYWORD];
        scanf("%s", keyword);
        insert(&ht, keyword);
    }

    char blog_keyword[NUM_OF_KEYWORD][200];
    int remaining = n;

    // 블로그 키워드 처리
    for (int i = 0; i < m; i++) {
        scanf("%s", blog_keyword[i]);
        
        char* token = strtok(blog_keyword[i], ",");
        while (token) {
            if (searchAndRemove(&ht, token)) {
                remaining--;
            }
            token = strtok(NULL, ",");
        }
        printf("%d\n", remaining);
    }

    freeHashTable(&ht);
    return 0;
}