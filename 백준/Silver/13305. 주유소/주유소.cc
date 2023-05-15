#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;  // 도시의 개수

    vector<int> distances(N);
    for (int i = 0; i < N; i++) {
        cin >> distances[i];
    }

    vector<int> costs(N);
    for (int i = 0; i < N; i++) {
        cin >> costs[i];
    }

    int money = 0;
    int a = 0, i = 0;

    while (i < N) {
        bool state = false;

        if (i == N - 1 && a == N - 1) {  // i가 마지막일 때
            i = a;
        } else if (i == N - 1 && a != N - 1) {
            money += costs[i] * distances[i - 1];
        }

        for (int j = i + 1; j < N; j++) {
            if (costs[i] >= costs[j] || j == N - 1) {
                int sum = 0;
                for (int k = i; k < j; k++) {
                    sum += distances[k];
                }
                money += costs[i] * sum;
                state = true;
                a = j;
                break;
            }
        }

        if (state) {
            i = a;
        } else {
            i += 1;
        }
    }

    cout << money << endl;

    return 0;
}
