#include <string.h>
#include <stdio.h>

int max(a, b) {
  if(a >= b) return a;
  else return b;
}

int main(void) {
  int n;
  int header[101];
  int ans;
  int temp;
  
  scanf("%d", &n);
  for(int i=0; i<n; i++) {
    scanf("%d", header+i);
  }

  ans = -1;
  for(int i=2; i<100; i++) {
    temp = 0;
    for(int j=0; j<n; j++) {
      if(header[j]%i == 0) temp++;
    }
    ans = max(ans, temp);
  }
  printf("%d", ans);
  return 0;
}
