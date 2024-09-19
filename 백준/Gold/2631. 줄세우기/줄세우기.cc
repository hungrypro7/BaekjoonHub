#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    int line[n];
    for (int i=0; i<n; i++) {
        cin >> line[i];
    }
    
    int dp[n];
    for (int i=0; i<n; i++) {
        dp[i] = 1;
    }
    
    int temp;
    for (int i=0; i<n; i++) {
        temp = 0;
        for (int j=i-1; j>-1; j--) {
            if (line[j] < line[i]) {
                temp = max(temp, dp[j]);
            }
        }
        dp[i] += temp;
    }
    
    cout << n - *max_element(dp, dp+n) << endl;
    return 0;
}
