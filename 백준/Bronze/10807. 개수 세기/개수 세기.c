#include <stdio.h>

int main(void) {
    
    int n;    // 정수의 개수
    scanf("%d", &n);
    
    int arr[n];    // 정수 입력 배열
    for(int i=0; i<n; i++) {
      scanf("%d", &arr[i]);
    }

    int v;    // 찾으려고 하는 정수
    scanf("%d", &v);  

    int count = 0;
    for(int i=0; i<n; i++) {
      if(arr[i] == v) { count++; }
    }
  
    printf("%d\n", count);
    return 0;
}