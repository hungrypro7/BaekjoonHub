#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<std::vector<int>> rgb(n, std::vector<int>(3));
    const int INF = 2147000000;
    int ans = INF;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cin >> rgb[i][j];
        }
    }

    for (int i = 0; i < 3; ++i) {
        std::vector<std::vector<int>> dp(n, std::vector<int>(3, INF));
        dp[0][i] = rgb[0][i];

        for (int j = 1; j < n; ++j) {
            dp[j][0] = std::min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0];
            dp[j][1] = std::min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1];
            dp[j][2] = std::min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2];
        }

        for (int j = 0; j < 3; ++j) {
            if (i != j) {
                ans = std::min(ans, dp[n - 1][j]);
            }
        }
    }

    std::cout << ans << std::endl;

    return 0;
}
