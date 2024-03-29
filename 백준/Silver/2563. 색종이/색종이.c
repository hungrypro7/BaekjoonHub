#include <stdio.h>

int main(void) {
  int n;
  scanf("%d", &n);
  int square[101][101] = {0 ,};

  int x, y;
  for(int i=0; i<n; i++) {
    scanf("%d %d", &x, &y);
    for(int j=x-1; j<x+9; j++) {
      for(int k=y-1; k<y+9; k++) {
        if(square[j][k] != 1)  square[j][k] = 1;
      }
    }
  }

  int ans = 0;
  for(int i=0; i<101; i++)
    for(int j=0; j<101; j++) 
      ans += square[i][j];

  printf("%d", ans);
  return 0;
}