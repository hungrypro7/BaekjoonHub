#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

int main() {
    std::string s;
    std::cin >> s;

    // 문자열 'a'의 개수를 센다.
    int a = std::count(s.begin(), s.end(), 'a');

    // 원형 문자열 생성
    s += s.substr(0, a - 1);

    // 최솟값을 큰 값으로 초기화
    int min_val = INT_MAX;

    // 슬라이딩 윈도우 방식으로 문자열의 각 부분을 체크
    for (int i = 0; i <= s.length() - a; ++i) {
        int count_b = std::count(s.begin() + i, s.begin() + i + a, 'b');
        min_val = std::min(min_val, count_b);
    }

    // 결과 출력
    std::cout << min_val << std::endl;

    return 0;
}