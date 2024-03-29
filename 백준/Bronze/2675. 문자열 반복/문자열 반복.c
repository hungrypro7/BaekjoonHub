#include <stdio.h>
#include <string.h>

int main(void) {
  int t;
  scanf("%d", &t);
  
  int r;
  int cnt;
  char st[21];
  
  for(int i=0; i<t; i++) {
    scanf("%d", &r);
    scanf("%s", st);
    cnt = 0;
    for(int j=0; j<21; j++) {
       if(st[j] != '\0') cnt++; 
       else break;
    }
    
    for(int j=0; j<cnt; j++) {
      for(int k=0; k<r; k++) {
        printf("%c", st[j]);
      }
    }
    printf("\n");
  }
}