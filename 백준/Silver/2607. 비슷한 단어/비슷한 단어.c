#include <stdio.h>
#include <string.h>

#define MAX_LEN 101

int main() {
    int n, count = 0;
    char target[MAX_LEN], word[MAX_LEN];
    
    scanf("%d", &n);
    scanf("%s", target);
    
    for (int i = 0; i < n - 1; i++) {
        scanf("%s", word);
        
        int target_freq[26] = {0}, word_freq[26] = {0};
        
        for (int j = 0; target[j] != '\0'; j++) {
            target_freq[target[j] - 'A']++;
        }
        
        for (int j = 0; word[j] != '\0'; j++) {
            word_freq[word[j] - 'A']++;
        }
        
        int add = 0, remove = 0;
        for (int j = 0; j < 26; j++) {
            if (target_freq[j] > word_freq[j]) {
                remove += target_freq[j] - word_freq[j];
            } else {
                add += word_freq[j] - target_freq[j];
            }
        }
        
        if (add < 2 && remove < 2) {
            count++;
        }
    }
    
    printf("%d\n", count);
    return 0;
}
