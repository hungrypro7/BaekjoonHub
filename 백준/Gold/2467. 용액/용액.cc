#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;    // 전체 용액의 수
    
    int sol[n];    // 용액의 특성값
    for(int i=0; i<n; i++) {
        cin >> sol[i];
    }
    
    int p, q;
    p = 0;
    q = n-1;
    
    int ans[2] = { 0, 0 };
    double temp = INFINITY;
    
    int two_sum = 0;
    while (p < q) {
        two_sum = sol[p] + sol[q];
        if (two_sum > 0){
            if (abs(two_sum) < temp) {
                temp = abs(two_sum);
                ans[0] = p;
                ans[1] = q;
            }
            q--;
        }
            
        else if (two_sum < 0) {
            if (abs(two_sum) < temp) {
                temp = abs(two_sum);
                ans[0] = p;
                ans[1] = q;
            }
            p++;
        }
        
        else {
            ans[0] = p;
            ans[1] = q;
            break;
        }
    }
    
    int front, end;
    front = ans[0];
    end = ans[1];
    
    cout << sol[front] << " " << sol[end] << endl;
    
}
