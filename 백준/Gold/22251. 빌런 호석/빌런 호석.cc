#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

vector<vector<int>> led = {
    {1, 1, 1, 0, 1, 1, 1}, // 0
    {0, 0, 1, 0, 0, 1, 0}, // 1
    {1, 0, 1, 1, 1, 0, 1}, // 2
    {1, 0, 1, 1, 0, 1, 1}, // 3
    {0, 1, 1, 1, 0, 1, 0}, // 4
    {1, 1, 0, 1, 0, 1, 1}, // 5
    {1, 1, 0, 1, 1, 1, 1}, // 6
    {1, 0, 1, 0, 0, 1, 0}, // 7
    {1, 1, 1, 1, 1, 1, 1}, // 8
    {1, 1, 1, 1, 0, 1, 1}  // 9
};

int compare(int a, int b) {
    
    int count = 0;
    string str1 = to_string(a);
    string str2 = to_string(b);
    
    int len1 = (int)str1.length();
    int len2 = (int)str2.length();
    
    if (len1 == len2) {
        for (int j = len1 - 1; j >= 0; --j) {
            int temp1 = str1[j] - '0';
            int temp2 = str2[j] - '0';
            for (int k = 0; k < 7; ++k) {
                if (led[temp1][k] != led[temp2][k]) {
                    count++;
                }
            }
        }
    }
    // 첫 번째 문자열이 더 긴 경우
    else if (len1 > len2) {
        str2 = string(len1 - len2, '0') + str2; // 앞에 '0'을 추가
        for (int j = len1 - 1; j >= 0; --j) {
            int temp1 = str1[j] - '0';
            int temp2 = str2[j] - '0';
            for (int k = 0; k < 7; ++k) {
                if (led[temp1][k] != led[temp2][k]) {
                    count++;
                }
            }
        }
    }
    // 두 번째 문자열이 더 긴 경우
    else {
        str1 = string(len2 - len1, '0') + str1; // 앞에 '0'을 추가
        for (int j = len2 - 1; j >= 0; --j) {
            int temp1 = str1[j] - '0';
            int temp2 = str2[j] - '0';
            for (int k = 0; k < 7; ++k) {
                if (led[temp1][k] != led[temp2][k]) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    
    int n, k, p, x;
    cin >> n >> k >> p >> x;
    
    int ans = 0;
    
    for(int i=1; i<n+1; i++) {
        if (i != x && compare(i, x) <= p)
            ans++;
    }
    
    cout << ans << endl;
    
    return 0;
}
