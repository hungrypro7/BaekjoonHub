#include <stdio.h>

int max(int a, int b) {
    if (a >= b) { return a; }
    else { return b; }
}

int main(void) {
    int t;
    scanf("%d", &t);
    
    int z[100] = {1, 0, 1};
    int o[100] = {0, 1, 1};
    
    int z_po = 3;
    int o_po = 3;
    
    for (int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        
        if (n >= 3) {
            for (int j=0; j<n-2; j++) {
                int temp1;
                temp1 = z[z_po-1] + z[z_po-2];
                if (z_po > 40) { continue; }
                z[z_po] = temp1;
                z_po++;
                
                int temp2;
                temp2 = o[o_po-1] + o[o_po-2];
                if (o_po > 40) { continue; }
                o[o_po] = temp2;
                o_po++;
            }
        }
        printf("%d %d\n", z[n], o[n]);
    }
    
    return 0;
}
