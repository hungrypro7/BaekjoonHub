#include <string.h>
#include <stdio.h>

int main(void) {
  int t;
  scanf("%d", &t);

  for(int i=0; i<t; i++){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n/5; i++) printf("++++ ");
    for(int i=0; i<n%5; i++) printf("|");
    printf("\n");
  }
}
