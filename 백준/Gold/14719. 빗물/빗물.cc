#include <iostream>
#include <vector>

using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    
    vector<int>block_height(w);
    for (int i=0; i<w; i++) {
        cin >> block_height[i];
    }
    
    vector<vector<int>> block(h, vector<int>(w, 0));
    
    for (int i=0; i<w; i++) {
        int bh = block_height[i];
        for (int j=0; j<bh; j++) {
            block[j][i] = 1;
        }
    }
    
    int water = 0;
    for (int i=0; i<h; i++) {
        int start = 0, end = 0;
        
        for (int k=0; k<w; k++) {    // 왼쪽
            if (block[i][k] == 1) {
                start = k;
                break;
            }
        }
        
        for (int k=w-1; k>-1; k--) {    // 오른쪽
            if (block[i][k] == 1) {
                end = k;
                break;
            }
        }
        
        if (start == end) {
            continue;
        }
        
        for (int k=start; k<end; k++) {
            if (block[i][k] == 0) {
                water++;
            }
        }
    }
    
    cout << water << endl;
    
    return 0;
}
