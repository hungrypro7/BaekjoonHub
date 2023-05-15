#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    
    std::vector<int> lope;
    for (int i = 0; i < n; i++) {
        int k;
        std::cin >> k;
        lope.push_back(k);
    }
    
    std::sort(lope.begin(), lope.end());
    
    int max = 0;
    for (int i : lope) {
        if (i > max) {
            max = i;
        }
    }
    
    for (int j = 1; j <= lope.size(); j++) {
        if ((lope.size() - j + 1) * lope[j-1] > max) {
            max = (lope.size() - j + 1) * lope[j-1];
        }
    }
    
    std::cout << max << std::endl;
    
    return 0;
}
